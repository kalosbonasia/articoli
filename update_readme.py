from pathlib import Path

ARTICOLI_DIR = Path("articoli")
README_PATH = Path("README.md")

INTRO = """# Raccolta articoli di Kalos

Indice degli articoli
"""

def genera_lista():
    files = sorted(ARTICOLI_DIR.glob("*.md"))
    righe = []
    for file in files:
        nome = file.stem.replace("-", " ")
        link = f"articoli/{file.name}"
        righe.append(f"* [{nome}]({link})")
    return "\n".join(righe)

def main():
    contenuto = INTRO.strip() + "\n\n" + genera_lista() + "\n"
    README_PATH.write_text(contenuto, encoding="utf-8")

if __name__ == "__main__":
    main()
