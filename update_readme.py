from pathlib import Path

ARTICOLI_DIR = Path("articoli")
README_PATH = Path("README.md")

INTRO = """# Raccolta articoli di Kalos

Indice degli articoli
"""

def estrai_titolo(md_path):
    with md_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip("# ").strip()
    return md_path.stem.replace("-", " ").capitalize()  # fallback

def genera_lista():
    files = sorted(ARTICOLI_DIR.glob("*.md"), reverse=False)  # puoi cambiare in reverse=True se vuoi ordine inverso
    righe = []
    for file in files:
        titolo = estrai_titolo(file)
        link = f"articoli/{file.name}"
        righe.append(f"* [{titolo}]({link})")
    return "\n".join(righe)

def main():
    contenuto = INTRO.strip() + "\n\n" + genera_lista() + "\n"
    R
