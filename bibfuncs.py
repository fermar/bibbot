import json
from pathlib import Path

# Función para cargar la Biblia desde un archivo JSON
def cargar_biblia(archivo: str = "es_rvr1960.json") -> list:
    RUTA = Path(__file__).parent / archivo
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            biblia = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"No encuentro el archivo: {RUTA}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"El JSON está mal formado: {e}")
    return biblia