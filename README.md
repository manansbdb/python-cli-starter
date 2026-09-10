# Python CLI Starter / Starter de CLI em Python

## Overview / Visão geral

**EN:** Minimal `argparse` CLI skeleton with an example `requirements.txt`.

**PT:** Esqueleto mínimo de CLI com `argparse` e um `requirements.txt` de exemplo.

## Layout

```
cli/
  __init__.py
  __main__.py   # python -m cli
  main.py       # argparse entry
requirements.txt
```

## Usage / Uso

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m cli --help
python -m cli greet --name Ada
```

**EN:** Extend `main.py` with new subcommands as needed.

**PT:** Estende `main.py` com novos subcomandos conforme necessário.

## License / Licença

MIT © 2026 manansbdb

## Support / Apoio

See [SUPPORT.md](SUPPORT.md) · Ver [SUPPORT.md](SUPPORT.md).
