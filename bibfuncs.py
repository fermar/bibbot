import json
from pathlib import Path


def cargar_biblia():
    RUTA = Path(__file__).parent / "es_rvr1960.json"
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            biblia = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"No encuentro el archivo: {RUTA}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"El JSON está mal formado: {e}")
    return biblia