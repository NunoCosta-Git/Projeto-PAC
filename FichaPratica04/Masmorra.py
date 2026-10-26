
class Masmorra:
    # Guarda a informação de uma masmorra, incluindo o nome, a descrição e os caminhos que pode seguir.
    def __init__(self, numero, nome, descricao, caminhosDisponiveis=None):
        self.__numero = numero
        self.__nome = nome
        self.__descricao = descricao
        self.__caminhosDisponiveis = caminhosDisponiveis or []

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getDescricao(self):
        return self.__descricao

    def getCaminhosDisponiveis(self):
        return self.__caminhosDisponiveis

    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setCaminhosDisponiveis(self, caminhosDisponiveis):
        self.__caminhosDisponiveis = caminhosDisponiveis

    def mostrarInformacao(self):
        print("\n===== MASMORRA ATUAL =====")
        print("Número:", self.__numero)
        print("Nome:", self.__nome)
        print("Descrição:", self.__descricao)

    def mostrarInfo(self):
        self.mostrarInformacao()

    def mostrarCaminhosDisponiveis(self):
        if len(self.__caminhosDisponiveis) == 0:
            print("Não há caminhos disponíveis a partir desta masmorra.")
            return

        print("\nCaminhos disponíveis a partir desta masmorra:")
        for caminho in self.__caminhosDisponiveis:
            print(f"- Masmorra {caminho}")
