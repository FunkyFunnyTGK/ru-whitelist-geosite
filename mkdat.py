# Build a v2ray/xray geosite .dat (GeoSiteList protobuf) without dependencies.
# GeoSiteList{1: repeated GeoSite}; GeoSite{1: country_code, 2: repeated Domain}
# Domain{1: type (0 Plain,1 Regex,2 Domain,3 Full), 2: value}
import sys
def varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F; n >>= 7
        out.append(b | (0x80 if n else 0))
        if not n: return bytes(out)
def field_bytes(num, data): return varint(num << 3 | 2) + varint(len(data)) + data
def field_varint(num, v): return varint(num << 3 | 0) + varint(v)
def domain(t, v):
    return (field_varint(1, t) if t else b"") + field_bytes(2, v.encode())
def site(code, doms):
    body = field_bytes(1, code.upper().encode())
    for t, v in doms: body += field_bytes(2, domain(t, v))
    return body
out = sys.argv[1]; cats = {}
for spec in sys.argv[2:]:          # name=path_to_txt (one suffix per line)
    name, path = spec.split("=", 1)
    ds = sorted({l.strip().lower() for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")})
    cats[name] = [(2, d) for d in ds]
cats["private"] = [(2, d) for d in ("local", "localhost", "lan", "home.arpa", "internal")]
data = b"".join(field_bytes(1, site(n, d)) for n, d in cats.items())
open(out, "wb").write(data)
print({k: len(v) for k, v in cats.items()}, len(data), "bytes")
