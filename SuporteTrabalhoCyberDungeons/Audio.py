import os
import pygame


class Audio:
    """
    Classe utilitária para tocar soundtrack e efeitos sonoros.
    Não é necessário criar objetos desta classe.
    """

    soundtrack_atual = None
    efeitos_ativos = []
    mixer_iniciado = False

    @staticmethod
    def inicializar_mixer():
        """
        Inicializa o mixer do pygame, caso ainda não tenha sido inicializado.
        """
        if not Audio.mixer_iniciado:
            pygame.mixer.init()
            Audio.mixer_iniciado = True

    @staticmethod
    def verificar_ficheiro(caminho: str):
        """
        Verifica se o ficheiro existe.
        """
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Ficheiro não encontrado: {caminho}")

    @staticmethod
    def play_soundtrack(caminho: str):
        """
        Toca uma soundtrack em loop.
        """
        try:
            Audio.inicializar_mixer()
            Audio.verificar_ficheiro(caminho)

            Audio.stop_soundtrack()

            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play(-1)

            Audio.soundtrack_atual = caminho

        except Exception as e:
            print("Erro ao tocar soundtrack:", e)

    @staticmethod
    def change_soundtrack(caminho: str):
        """
        Troca a soundtrack atual por outra.
        Se a mesma soundtrack já estiver a tocar, não faz nada.
        """
        if (
            Audio.soundtrack_atual == caminho
            and Audio.is_soundtrack_playing()
        ):
            return

        Audio.play_soundtrack(caminho)

    @staticmethod
    def stop_soundtrack():
        """
        Para a soundtrack atual.
        """
        try:
            if Audio.mixer_iniciado:
                pygame.mixer.music.stop()
                Audio.soundtrack_atual = None

        except Exception as e:
            print("Erro ao parar soundtrack:", e)

    @staticmethod
    def play_effect(caminho: str):
        """
        Toca um efeito sonoro por cima da soundtrack.
        """
        try:
            Audio.inicializar_mixer()
            Audio.verificar_ficheiro(caminho)

            efeito = pygame.mixer.Sound(caminho)
            canal = efeito.play()

            if canal is not None:
                Audio.efeitos_ativos.append((canal, efeito))

            Audio.limpar_efeitos_terminados()

        except Exception as e:
            print("Erro ao tocar efeito sonoro:", e)

    @staticmethod
    def limpar_efeitos_terminados():
        """
        Remove da lista os efeitos que já terminaram.
        """
        Audio.efeitos_ativos = [
            (canal, efeito)
            for canal, efeito in Audio.efeitos_ativos
            if canal.get_busy()
        ]

    @staticmethod
    def stop_all_effects():
        """
        Para todos os efeitos sonoros.
        """
        try:
            for canal, efeito in Audio.efeitos_ativos:
                canal.stop()

            Audio.efeitos_ativos.clear()

        except Exception as e:
            print("Erro ao parar efeitos sonoros:", e)

    @staticmethod
    def stop_all():
        """
        Para todos os áudios.
        """
        Audio.stop_soundtrack()
        Audio.stop_all_effects()

    @staticmethod
    def is_soundtrack_playing() -> bool:
        """
        Verifica se a soundtrack está a tocar.
        """
        if not Audio.mixer_iniciado:
            return False

        return pygame.mixer.music.get_busy()