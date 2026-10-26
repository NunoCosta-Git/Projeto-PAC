import os
import time
from pathlib import Path

try:
    import winsound
except ImportError:
    winsound = None


# ============================================================
# CLASSE RECURSOS
# ============================================================

class Recursos:

    @staticmethod
    def limparConsola():
        # No PyCharm, os comandos cls/clear nem sempre limpam bem a consola.
        # Esta solução é mais simples e funciona em praticamente todos os ambientes.
        print("\n" * 100)

    @staticmethod
    def pausa(segundos):
        # Faz uma pausa na execução do programa.
        # Serve para dar mais ritmo à narrativa do jogo.
        time.sleep(segundos)

    @staticmethod
    def imprimirAscii(caminhoFicheiro, textoAlternativo=""):
        # Tenta imprimir o conteúdo de um ficheiro ASCII.
        # Se o ficheiro não existir, mostra um texto alternativo.

        caminho = Path(caminhoFicheiro)
        if not caminho.is_absolute():
            caminho = Path(__file__).resolve().parent / caminhoFicheiro

        if caminho.exists():
            try:
                with open(caminho, "r", encoding="utf-8") as ficheiro:
                    conteudo = ficheiro.read()
                    print(conteudo)
            except Exception:
                print(textoAlternativo)
        else:
            print(textoAlternativo)

    @staticmethod
    def tocarAudio(caminhoFicheiro):
        # Tenta tocar um ficheiro de áudio .wav.
        # O winsound funciona apenas em Windows.
        # Se não for possível tocar áudio, o programa continua normalmente.

        if winsound is None:
            return

        if os.path.exists(caminhoFicheiro):
            try:
                winsound.PlaySound(
                    caminhoFicheiro,
                    winsound.SND_FILENAME | winsound.SND_ASYNC
                )
            except Exception:
                pass

    @staticmethod
    def tocarAudioBloqueante(caminhoFicheiro):
        # Toca um áudio e espera que ele termine antes de continuar.
        # Pode ser útil para sons curtos, como vitória ou derrota.

        if winsound is None:
            return

        if os.path.exists(caminhoFicheiro):
            try:
                winsound.PlaySound(
                    caminhoFicheiro,
                    winsound.SND_FILENAME
                )
            except Exception:
                pass

    @staticmethod
    def pararAudio():
        # Para qualquer áudio que esteja a tocar.
        # Só funciona se winsound estiver disponível.

        if winsound is not None:
            try:
                winsound.PlaySound(None, 0)
            except Exception:
                pass

    @staticmethod
    def esperarEnter(mensagem="Pressiona ENTER para continuar..."):
        # Pausa o jogo até o utilizador carregar em ENTER.
        input("\n" + mensagem)

    @staticmethod
    def imprimirLinha(tamanho=40, simbolo="="):
        # Imprime uma linha decorativa.
        print(simbolo * tamanho)

    @staticmethod
    def imprimirTitulo(titulo):
        # Imprime um título formatado para a consola.

        Recursos.imprimirLinha()
        print(titulo.center(40))
        Recursos.imprimirLinha()