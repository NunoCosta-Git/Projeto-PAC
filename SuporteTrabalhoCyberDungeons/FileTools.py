class FileTools:
    """
    Classe utilitária para trabalhar com ficheiros de texto.
    Não é necessário criar objetos desta classe.
    """

    @staticmethod
    def print_file(path: str):
        """
        Lê um ficheiro de texto e imprime o seu conteúdo linha a linha.
        """

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")