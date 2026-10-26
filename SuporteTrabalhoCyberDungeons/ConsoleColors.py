class ConsoleColors:
    """
    Classe utilitária para imprimir texto colorido na consola usando códigos ANSI.
    Não é necessário criar objetos desta classe.
    """

    colors_enabled = True

    # Escape ANSI
    ESC = "\033["

    # Reset
    RESET = ESC + "0m"

    # Estilos
    BOLD = ESC + "1m"
    UNDERLINE = ESC + "4m"
    REVERSED = ESC + "7m"

    # Regular Colors
    BLACK = ESC + "0;30m"
    RED = ESC + "0;31m"
    GREEN = ESC + "0;32m"
    YELLOW = ESC + "0;33m"
    BLUE = ESC + "0;34m"
    PURPLE = ESC + "0;35m"
    CYAN = ESC + "0;36m"
    WHITE = ESC + "0;37m"

    # Bold Colors
    BLACK_BOLD = ESC + "1;30m"
    RED_BOLD = ESC + "1;31m"
    GREEN_BOLD = ESC + "1;32m"
    YELLOW_BOLD = ESC + "1;33m"
    BLUE_BOLD = ESC + "1;34m"
    PURPLE_BOLD = ESC + "1;35m"
    CYAN_BOLD = ESC + "1;36m"
    WHITE_BOLD = ESC + "1;37m"

    # Underline Colors
    BLACK_UNDERLINED = ESC + "4;30m"
    RED_UNDERLINED = ESC + "4;31m"
    GREEN_UNDERLINED = ESC + "4;32m"
    YELLOW_UNDERLINED = ESC + "4;33m"
    BLUE_UNDERLINED = ESC + "4;34m"
    PURPLE_UNDERLINED = ESC + "4;35m"
    CYAN_UNDERLINED = ESC + "4;36m"
    WHITE_UNDERLINED = ESC + "4;37m"

    # Background Colors
    BLACK_BACKGROUND = ESC + "40m"
    RED_BACKGROUND = ESC + "41m"
    GREEN_BACKGROUND = ESC + "42m"
    YELLOW_BACKGROUND = ESC + "43m"
    BLUE_BACKGROUND = ESC + "44m"
    PURPLE_BACKGROUND = ESC + "45m"
    CYAN_BACKGROUND = ESC + "46m"
    WHITE_BACKGROUND = ESC + "47m"

    # Bright Colors
    BLACK_BRIGHT = ESC + "0;90m"
    RED_BRIGHT = ESC + "0;91m"
    GREEN_BRIGHT = ESC + "0;92m"
    YELLOW_BRIGHT = ESC + "0;93m"
    BLUE_BRIGHT = ESC + "0;94m"
    PURPLE_BRIGHT = ESC + "0;95m"
    CYAN_BRIGHT = ESC + "0;96m"
    WHITE_BRIGHT = ESC + "0;97m"

    # Bold Bright Colors
    BLACK_BOLD_BRIGHT = ESC + "1;90m"
    RED_BOLD_BRIGHT = ESC + "1;91m"
    GREEN_BOLD_BRIGHT = ESC + "1;92m"
    YELLOW_BOLD_BRIGHT = ESC + "1;93m"
    BLUE_BOLD_BRIGHT = ESC + "1;94m"
    PURPLE_BOLD_BRIGHT = ESC + "1;95m"
    CYAN_BOLD_BRIGHT = ESC + "1;96m"
    WHITE_BOLD_BRIGHT = ESC + "1;97m"

    # Bright Backgrounds
    BLACK_BACKGROUND_BRIGHT = ESC + "0;100m"
    RED_BACKGROUND_BRIGHT = ESC + "0;101m"
    GREEN_BACKGROUND_BRIGHT = ESC + "0;102m"
    YELLOW_BACKGROUND_BRIGHT = ESC + "0;103m"
    BLUE_BACKGROUND_BRIGHT = ESC + "0;104m"
    PURPLE_BACKGROUND_BRIGHT = ESC + "0;105m"
    CYAN_BACKGROUND_BRIGHT = ESC + "0;106m"
    WHITE_BACKGROUND_BRIGHT = ESC + "0;107m"

    @staticmethod
    def set_colors_enabled(enabled: bool):
        """
        Permite ligar ou desligar as cores.
        """
        ConsoleColors.colors_enabled = enabled

    @staticmethod
    def colorize(text: str, color: str) -> str:
        """
        Aplica uma cor/estilo a um texto.
        """
        if not ConsoleColors.colors_enabled:
            return text

        return color + text + ConsoleColors.RESET

    @staticmethod
    def print(text: str, color: str):
        """
        Imprime texto colorido sem mudar de linha.
        """
        print(ConsoleColors.colorize(text, color), end="")

    @staticmethod
    def println(text: str, color: str):
        """
        Imprime texto colorido com mudança de linha.
        """
        print(ConsoleColors.colorize(text, color))

    @staticmethod
    def error(text: str):
        """
        Mensagem de erro.
        """
        ConsoleColors.println("❌ " + text, ConsoleColors.RED_BOLD_BRIGHT)

    @staticmethod
    def success(text: str):
        """
        Mensagem de sucesso.
        """
        ConsoleColors.println("✅ " + text, ConsoleColors.GREEN_BOLD_BRIGHT)

    @staticmethod
    def warning(text: str):
        """
        Mensagem de aviso.
        """
        ConsoleColors.println("⚠️ " + text, ConsoleColors.YELLOW_BOLD_BRIGHT)

    @staticmethod
    def info(text: str):
        """
        Mensagem informativa.
        """
        ConsoleColors.println("ℹ️ " + text, ConsoleColors.CYAN_BOLD_BRIGHT)

    @staticmethod
    def game(text: str):
        """
        Mensagem normal de jogo.
        """
        ConsoleColors.println(text, ConsoleColors.WHITE_BOLD)

    @staticmethod
    def story(text: str):
        """
        Mensagem narrativa.
        """
        ConsoleColors.println(text, ConsoleColors.PURPLE_BRIGHT)

    @staticmethod
    def title(text: str):
        """
        Título simples.
        """
        print()
        ConsoleColors.println("═" * (len(text) + 8), ConsoleColors.YELLOW_BOLD_BRIGHT)
        ConsoleColors.println("   " + text + "   ", ConsoleColors.YELLOW_BOLD_BRIGHT)
        ConsoleColors.println("═" * (len(text) + 8), ConsoleColors.YELLOW_BOLD_BRIGHT)
        print()

    @staticmethod
    def box(text: str, color: str):
        """
        Cria uma caixa simples à volta do texto.
        """
        line = "═" * (len(text) + 4)

        ConsoleColors.println("╔" + line + "╗", color)
        ConsoleColors.println("║  " + text + "  ║", color)
        ConsoleColors.println("╚" + line + "╝", color)

    @staticmethod
    def separator():
        """
        Imprime uma linha separadora.
        """
        ConsoleColors.println("─" * 50, ConsoleColors.BLACK_BRIGHT)

    @staticmethod
    def clear():
        """
        Limpa a consola.
        Pode não funcionar em todos os ambientes.
        """
        print(ConsoleColors.ESC + "H" + ConsoleColors.ESC + "2J", end="")

    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:
        """
        Permite usar cor RGB personalizada.
        Nem todas as consolas suportam isto.
        """
        return ConsoleColors.ESC + f"38;2;{r};{g};{b}m"

    @staticmethod
    def background_rgb(r: int, g: int, b: int) -> str:
        """
        Permite usar fundo RGB personalizado.
        """
        return ConsoleColors.ESC + f"48;2;{r};{g};{b}m"