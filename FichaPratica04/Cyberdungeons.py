# ============================================================
# CYBERDUNGEONS
# Ficha Prática de Programação Orientada a Objetos em Python
#
# Tema:
# Uma personagem do ano 2077 viaja acidentalmente para o ano 1272
# após uma ruptura temporal. Para regressar à sua realidade,
# terá de atravessar masmorras medievais e encontrar a máquina do tempo.
#
# Regras da ficha:
# - Utilizar atributos privados
# - Utilizar getters e setters tradicionais
# - Completar os métodos assinalados com TODO
# ============================================================
import sys
from pathlib import Path

PASTA_ATUAL = Path(__file__).resolve().parent
if str(PASTA_ATUAL) not in sys.path:
    sys.path.append(str(PASTA_ATUAL))

try:
    from .Jogo import Jogo
except ImportError:
    from Jogo import Jogo


def main():
    jogo = Jogo()
    jogo.iniciarJogo()


if __name__ == "__main__":
    main()