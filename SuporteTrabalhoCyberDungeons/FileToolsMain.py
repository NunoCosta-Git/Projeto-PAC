from pathlib import Path
from FileTools import FileTools


def main():
    # Pasta onde está este ficheiro FileToolsMain.py
    BASE_DIR = Path(__file__).resolve().parent

    # Pasta dos ficheiros de texto
    IMAGES_DIR = BASE_DIR / "resources" / "images"

    # Caminhos dos ficheiros
    castle_path = IMAGES_DIR / "castle.txt"
    dino_path = IMAGES_DIR / "dino.txt"

    print("CASTELO:")
    FileTools.print_file(str(castle_path))

    print()
    print("DINO:")
    FileTools.print_file(str(dino_path))


if __name__ == "__main__":
    main()