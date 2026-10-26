class Inimigo:
    # Representa os adversários que o jogador encontra nas masmorras.
    def __init__(self, nome, vida, ataque, defesa, experiencia, moedas):
        self.__nome = nome
        self.__vida = vida
        self.__ataque = ataque
        self.__defesa = defesa
        self.__experiencia = experiencia
        self.__moedas = moedas

    def getNome(self):
        return self.__nome

    def getVida(self):
        return self.__vida

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        return self.__moedas

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = vida

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    def receberDano(self, dano):
        # 1. Calcular o dano real recebido pelo inimigo.
        # 2. O dano real deve ter em conta a defesa do inimigo.
        # 3. O dano mínimo deve ser 1.
        # 4. Atualizar a vida do inimigo.
        # 5. Garantir que a vida não fica abaixo de 0.

        danoAplicado = dano - self.__defesa

        if danoAplicado > 0:

            if danoAplicado > self.__vida:
                self.__vida = 0
            else:
                self.__vida -= danoAplicado

            print(f"{self.__nome} recebeu {danoAplicado} dano.")
        else:
            print(f"A defesa do {self.__nome} é mais alta que o teu ataque. Não sofreu dano.")

    def atacar(self, jogador):
        # 1. Calcular o dano causado ao jogador.
        # 2. Chamar o método receberDano() do jogador.
        # 3. Mostrar uma mensagem com o ataque.

        print(f"{self.__nome} tentou atacar com {self.__ataque} de dano.")
        jogador.receberDano(self.__ataque)

    def estaVivo(self):
        # Devolver True se a vida do inimigo for maior do que 0.
        # Devolver False caso contrário.

        return self.__vida > 0

    def mostrarEstado(self):
        print("\n===== ESTADO DO INIMIGO =====")
        print("Nome:", self.__nome)
        print("Vida:", self.__vida)
        print("Ataque:", self.__ataque)
        print("Defesa:", self.__defesa)
