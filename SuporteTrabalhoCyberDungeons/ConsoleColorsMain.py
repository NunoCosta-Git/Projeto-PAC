from SuporteTrabalhoCyberDungeons.ConsoleColors import ConsoleColors


def main():
    ConsoleColors.title("Really Epic and Confusing Game")

    ConsoleColors.story("A tua aventura começa numa montanha misteriosa... ⛰️")
    ConsoleColors.game("Encontraste uma coroa perdida! 👑")

    ConsoleColors.success("Ganhaste 100 moedas!")
    ConsoleColors.warning("A tua vida está baixa!")
    ConsoleColors.error("Invalid choice!")
    ConsoleColors.info("Dica: talvez não devas atacar o dragão com uma colher.")

    ConsoleColors.separator()

    ConsoleColors.println("Texto azul brilhante", ConsoleColors.BLUE_BOLD_BRIGHT)
    ConsoleColors.println("Texto sublinhado", ConsoleColors.YELLOW_UNDERLINED)
    ConsoleColors.println("Fundo espetacular", ConsoleColors.CYAN_BACKGROUND_BRIGHT)

    ConsoleColors.box("BOSS FINAL", ConsoleColors.RED_BOLD_BRIGHT)

    ConsoleColors.println(
        "Texto com RGB personalizado",
        ConsoleColors.rgb(255, 120, 0)
    )


if __name__ == "__main__":
    main()