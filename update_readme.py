from pathlib import Path

ARTICOLI_DIR = Path("articoli")
README_PATH = Path("README.md")

INTRO = """# Raccolta articoli di Kalos

Indice degli articoli numerato
"""

def estrai_titolo(md_path):
    try:
        with md_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    print(f"[OK] Titolo estratto da {md_path.name}: {line[2:].strip()}")
                    return line[2:].strip()
        print(f"[WARN] Nessun titolo trovato in {md_path.name}, uso fallback.")
    except Exception as e:
        print(f"[ERROR] Errore leggendo {md_path.name}: {e}")
    return md_path.stem.replace("-", " ").capitalize()

def genera_lista():
    articoli = []
    for file in ARTICOLI_DIR.glob("*.md"):
        titolo = estrai_titolo(file)
        articoli.append((titolo.lower(), titolo, file.name))

    articoli.sort()  # ordina alfabeticamente per titolo (case-insensitive)

    righe = [
        f"{i + 1}. [{titolo}]({ARTICOLI_DIR / filename})"
        for i, (_, titolo, filename) in enumerate(articoli)
    ]
    return "\n".join(righe)

def main():
    print("🟢 Inizio generazione README.md")
    contenuto = INTRO.strip() + "\n\n" + genera_lista() + "\n"
    README_PATH.write_text(contenuto, encoding="utf-8")
    print("✅ README.md aggiornato con successo.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Errore imprevisto durante l'esecuzione: {e}")
        exit(1)
