# ru-whitelist-geosite

`geosite`-файл для Xray с доменами из белых списков мобильного интернета РФ.
Собирается ежедневно из [ancored/ru-mobile-whitelist](https://github.com/ancored/ru-mobile-whitelist).

## Файл

```
https://github.com/FunkyFunnyTGK/ru-whitelist-geosite/releases/latest/download/ru-whitelist.dat
```

Категории:

- `ru-whitelist` — домены из белого списка (совпадение по домену и поддоменам)
- `private` — `local`, `localhost`, `lan`, `home.arpa`, `internal`

## Использование в Xray

Положите файл в папку ресурсов клиента и используйте:

```json
{
  "domain": ["ext:ru-whitelist.dat:ru-whitelist", "ext:ru-whitelist.dat:private"],
  "outboundTag": "direct"
}
```

## Сборка вручную

```bash
python3 mkdat.py ru-whitelist.dat ru-whitelist=sni.txt
python3 readdat.py ru-whitelist.dat
```

Полнота и актуальность списка не гарантируются: белые списки различаются у операторов и регионов.
