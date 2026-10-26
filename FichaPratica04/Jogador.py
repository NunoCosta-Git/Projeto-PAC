class Jogador:
    # Representa o personagem do jogador e guarda as suas estatísticas, inventário e equipamento.
    def __init__(self, nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas):
        self.__nome = nome
        self.__vidaMaxima = vidaMaxima
        self.__vida = vidaMaxima
        self.__ataque = ataque
        self.__defesa = defesa
        self.__nivel = nivel
        self.__experiencia = experiencia
        self.__moedas = moedas
        self.__arma = None
        self.__armadura = None
        self.__inventarioPocoes = []
        self.__inventarioConsumiveisCombate = []
        self.__limiteInventario = 10

    def getNome(self):
        return self.__nome

    def getVida(self):
        return self.__vida

    def getVidaMaxima(self):
        return self.__vidaMaxima

    def getAtaque(self):
        return self.__ataque

    def getDefesa(self):
        return self.__defesa

    def getNivel(self):
        return self.__nivel

    def getExperiencia(self):
        return self.__experiencia

    def getMoedas(self):
        return self.__moedas

    def getArma(self):
        return self.__arma

    def getArmadura(self):
        return self.__armadura

    def getPocao(self):
        return self.__inventarioPocoes[0] if self.__inventarioPocoes else None

    def getInventarioPocoes(self):
        return self.__inventarioPocoes

    def getInventarioConsumiveisCombate(self):
        return self.__inventarioConsumiveisCombate

    def getLimiteInventario(self):
        return self.__limiteInventario

    def getTotalItensInventario(self):
        return len(self.__inventarioPocoes) + len(self.__inventarioConsumiveisCombate)

    def setNome(self, nome):
        self.__nome = nome

    def setVida(self, vida):
        self.__vida = vida

    def setVidaMaxima(self, vidaMaxima):
        self.__vidaMaxima = vidaMaxima

    def setAtaque(self, ataque):
        self.__ataque = ataque

    def setDefesa(self, defesa):
        self.__defesa = defesa

    def setNivel(self, nivel):
        self.__nivel = nivel

    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia

    def setMoedas(self, moedas):
        self.__moedas = moedas

    def setArma(self, arma):
        self.__arma = arma

    def setArmadura(self, armadura):
        self.__armadura = armadura

    def setPocao(self, pocao):
        self.guardarPocao(pocao)

    def getAtaqueTotal(self):
        if self.__arma is None:
            return self.__ataque
        return self.__ataque + self.__arma.getBonusAtaque()

    def getDefesaTotal(self):
        if self.__armadura is None:
            return self.__defesa
        return self.__defesa + self.__armadura.getBonusDefesa()

    def receberDano(self, dano):
        danoAplicado = dano - self.getDefesaTotal()
        if danoAplicado < 1:
            danoAplicado = 1
        self.__vida -= danoAplicado
        if self.__vida < 0:
            self.__vida = 0
        print(f"{self.__nome} recebeu {danoAplicado} dano.")

    def atacar(self, inimigo):
        dano = self.getAtaqueTotal()
        print(f"{self.__nome} atacou com {dano} de dano.")
        inimigo.receberDano(dano)

    def curar(self, valor):
        vidaAntes = self.__vida
        self.__vida += valor
        if self.__vida > self.__vidaMaxima:
            self.__vida = self.__vidaMaxima
        vidaRecuperada = self.__vida - vidaAntes
        print(f"{self.__nome} recuperou {vidaRecuperada} pontos de vida.")

    def ganharExperiencia(self, valor):
        self.__experiencia += valor
        print(f"{self.__nome} ganhou {valor} pontos de experiência.")
        self.subirNivel()

    def subirNivel(self):
        experienciaNecessaria = self.__nivel * 100
        if self.__experiencia >= experienciaNecessaria:
            self.__nivel += 1
            self.__vidaMaxima += 25
            self.__ataque += 4
            self.__defesa += 4
            self.__vida = self.__vidaMaxima
            self.__experiencia -= experienciaNecessaria
            print(f"{self.__nome} subiu para o nível {self.__nivel}!")
            return True
        return False

    def ganharMoedas(self, valor):
        self.__moedas += valor
        print(f"{self.__nome} recebeu {valor} moedas.")

    def gastarMoedas(self, valor):
        if self.__moedas >= valor:
            self.__moedas -= valor
            return True
        return False

    def equiparArma(self, arma):
        self.__arma = arma

    def equiparArmadura(self, armadura):
        self.__armadura = armadura

    def guardarPocao(self, pocao):
        if self.getTotalItensInventario() >= self.__limiteInventario:
            print(f"{self.__nome} não tem espaço no inventário para mais poções.")
            return False
        self.__inventarioPocoes.append(pocao)
        print(f"{self.__nome} guardou a poção {pocao.getNome()}.")
        return True

    def adicionarConsumivelCombate(self, consumivel):
        if self.getTotalItensInventario() >= self.__limiteInventario:
            print(f"{self.__nome} não tem espaço no inventário para mais consumíveis.")
            return False
        self.__inventarioConsumiveisCombate.append(consumivel)
        print(f"{self.__nome} guardou o consumível {consumivel.getNome()}.")
        return True

    def usarPocao(self):
        if len(self.__inventarioPocoes) == 0:
            print("Não tens poções para usar.")
            return False
        pocao = self.__inventarioPocoes.pop(0)
        self.curar(pocao.getValorCura())
        print(f"Usaste a poção {pocao.getNome()} e recuperaste {pocao.getValorCura()} vida.")
        return True

    def usarConsumivelCombate(self):
        if len(self.__inventarioConsumiveisCombate) == 0:
            print("Não tens consumíveis de combate para usar.")
            return 0
        consumivel = self.__inventarioConsumiveisCombate.pop(0)
        dano = consumivel.getDanoAleatorio()
        print(f"Usaste {consumivel.getNome()} e causaste {dano} de dano ao inimigo.")
        return dano

    def estaVivo(self):
        return self.__vida > 0

    def mostrarEstado(self):
        print("===== ESTADO DO JOGADOR =====")
        print("Nome:", self.__nome)
        print("Vida:", self.__vida, "/", self.__vidaMaxima)
        print("Nível:", self.__nivel)
        print("Experiência:", self.__experiencia)
        print("Moedas:", self.__moedas)
        print("Ataque base:", self.__ataque)
        print("Defesa base:", self.__defesa)
        print("Ataque total:", self.getAtaqueTotal())
        print("Defesa total:", self.getDefesaTotal())
        print("Poções no inventário:", len(self.__inventarioPocoes))
        print("Consumíveis de combate:", len(self.__inventarioConsumiveisCombate))
        print("Limite de inventário:", self.__limiteInventario)
        if self.__arma is None:
            print("Arma equipada: nenhuma")
        else:
            print("Arma equipada:", self.__arma.getNome())
        if self.__armadura is None:
            print("Armadura equipada: nenhuma")
        else:
            print("Armadura equipada:", self.__armadura.getNome())

    def mostrarEstadoResumido(self):
        print("===== ESTADO DO JOGADOR =====")
        print("Nome:", self.__nome)
        print("Vida:", self.__vida, "/", self.__vidaMaxima)
        print("Ataque total:", self.getAtaqueTotal())
        print("Defesa total:", self.getDefesaTotal())
        print("Poções no inventário:", len(self.__inventarioPocoes))
        print("Consumíveis de combate:", len(self.__inventarioConsumiveisCombate))
        if self.__arma is None:
            print("Arma equipada: nenhuma")
        else:
            print("Arma equipada:", self.__arma.getNome())
        if self.__armadura is None:
            print("Armadura equipada: nenhuma")
        else:
            print("Armadura equipada:", self.__armadura.getNome())