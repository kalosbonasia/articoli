from pathlib import Path

ARTICOLI_DIR = Path("articoli")
README_PATH = Path("README.md")

INTRO = """# Raccolta articoli di Kalos

Indice degli articoli
"""

def estrai_titolo(md_path):
    """
    Estrae il primo titolo Markdown (# ...) dal file.
    Se non lo trova, usa il nome del file come fallback.
    """
    try:
        with md_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception as e:
        print(f"Errore nel leggere {md_path.name}: {e}")
    # fallback
    return md_path.stem.replace("-", " ").capitalize()

def genera_lista():
    """
    Crea una lista puntata dei file Markdown presenti nella cartella 'articoli'.
    Ogni voce include un titolo (estratto



