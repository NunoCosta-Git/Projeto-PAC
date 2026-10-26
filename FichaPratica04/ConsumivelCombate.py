import random


class ConsumivelCombate:
    # Representa um item de combate com dano aleatório entre um mínimo e um máximo.
    def __init__(self, nome, danoMinimo, danoMaximo, preco):
        self.__nome = nome
        self.__danoMinimo = danoMinimo
        self.__danoMaximo = danoMaximo
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getDanoMinimo(self):
        return self.__danoMinimo

    def getDanoMaximo(self):
        return self.__danoMaximo

    def getPreco(self):
        return self.__preco

    def setNome(self, nome):
        self.__nome = nome

    def setDanoMinimo(self, danoMinimo):
        self.__danoMinimo = danoMinimo

    def setDanoMaximo(self, danoMaximo):
        self.__danoMaximo = danoMaximo

    def setPreco(self, preco):
        self.__preco = preco

    def getDanoAleatorio(self):
        return random.randint(self.__danoMinimo, self.__danoMaximo)

    def mostrarDados(self):
        print("Consumível de combate:", self.__nome)
        print("Dano mínimo:", self.__danoMinimo)
        print("Dano máximo:", self.__danoMaximo)
        print("Preço:", self.__preco, "moedas")
