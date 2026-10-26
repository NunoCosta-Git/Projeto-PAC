from time import sleep

try:
    from .Inimigo import Inimigo
    from .Jogador import Jogador
    from .Loja import Loja
    from .Masmorra import Masmorra
    from .Recursos import Recursos
except ImportError:
    from Inimigo import Inimigo
    from Jogador import Jogador
    from Loja import Loja
    from Masmorra import Masmorra
    from Recursos import Recursos


class Jogo:
    # Classe principal que controla o fluxo do jogo, as masmorras, os combates e a loja.
    def __init__(self):
        # Estado principal do jogo: jogador, masmorra atual, inimigo ativo e loja.
        self.__jogador = None
        self.__masmorraAtual = 1
        self.__inimigoAtual = None
        self.__loja = Loja()
        self.__terminado = False
        self.__descansosRestantes = 3

    def getJogador(self):
        return self.__jogador

    def getMasmorraAtual(self):
        return self.__masmorraAtual

    def getInimigoAtual(self):
        return self.__inimigoAtual

    def getLoja(self):
        return self.__loja

    def getTerminado(self):
        return self.__terminado

    def setJogador(self, jogador):
        self.__jogador = jogador

    def setMasmorraAtual(self, masmorraAtual):
        self.__masmorraAtual = masmorraAtual

    def setInimigoAtual(self, inimigoAtual):
        self.__inimigoAtual = inimigoAtual

    def setLoja(self, loja):
        self.__loja = loja

    def setTerminado(self, terminado):
        self.__terminado = terminado

    def iniciarJogo(self):
        self.mostrarIntroducao()

        nome = input("\nInsere o nome da tua personagem: ")

        if nome == "":
            nome = "Joaquim"
            print("Não escreveste nome. O sistema medieval atribuiu-te um nome altamente épico:")
            print("Joaquim.")

        self.criarJogador(nome)
        sleep(2)

        while self.__terminado is False:
            self.mostrarMenuPrincipal()
            opcao = input("Escolha: ")

            Recursos.limparConsola()

            if opcao == "1":
                self.__jogador.mostrarEstado()
                input("[Prima enter para continuar]")

            elif opcao == "2":
                self.explorarMasmorra()

            elif opcao == "3":
                self.visitarLoja()

            elif opcao == "4":
                self.descansar()

            elif opcao == "5":
                print("\nDecidiste sair do jogo.")
                print("A máquina do tempo fica para outro dia.")
                print("O ano 1272 agradece a tua curta visita.")
                self.__terminado = True

            else:
                print("\nOpção inválida.")
                print("Até no ano 1272 era esperado saber escolher uma opção do menu.")

    def mostrarIntroducao(self):
        Recursos.limparConsola()
        Recursos.tocarAudio("assets/audio/intro.wav")
        Recursos.imprimirAscii(
            "assets/ascii/logo.txt",
            """
    ======================================
               CYBERDUNGEONS
    ======================================
            """
        )

        Recursos.pausa(1)

        print("\nAno 2077.")
        Recursos.pausa(1)
        print("A humanidade finalmente conseguiu viajar no tempo.")
        Recursos.pausa(1)
        print("Infelizmente, alguém decidiu testar a máquina numa sexta-feira à tarde.")
        Recursos.pausa(1)
        print("Como seria de esperar, correu mal.")
        print()
        Recursos.pausa(1)
        print("Durante a viagem, ocorreu uma ruptura temporal.")
        print("A tua personagem foi enviada para o ano 1272.")
        print("Sem internet. Sem GPS. Sem carregador. Sem garantias.")
        print()
        Recursos.pausa(1)
        print("A máquina do tempo caiu algures no fundo de várias masmorras medievais.")
        print("Para regressares ao ano 2077, tens de sobreviver, lutar e recuperar o núcleo temporal.")
        print()
        Recursos.pausa(1)
        print("Bem-vindo a Cyberdungeons.")
        print("Um RPG medieval com problemas tecnológicos que ninguém pediu.")

    def criarJogador(self, nome):
        vidaMaxima = 100
        ataque = 10
        defesa = 5
        nivel = 1
        experiencia = 0
        moedas = 40

        self.__jogador = Jogador(nome, vidaMaxima, ataque, defesa, nivel, experiencia, moedas)

        print("\nPersonagem criada com sucesso.")
        print("Nome:", nome)
        print("Ano de origem: 2077")
        print("Ano atual: 1272")
        print("Estado emocional: confuso, mas funcional.")

    def mostrarMenuPrincipal(self):
        # Menu principal que permite ao jogador navegar pelas ações do jogo.
        Recursos.limparConsola()
        print("\n===== MENU PRINCIPAL =====")
        print("Masmorra atual:", self.__masmorraAtual)
        print("1 - Ver estado do jogador")
        print("2 - Explorar masmorra")
        print("3 - Visitar loja")
        print("4 - Descansar")
        print("5 - Sair")

    def obterNomeMasmorra(self, numero):
        # Converte um número de masmorra numa descrição legível para o jogador.
        nomes = {
            1: "Masmorra da Floresta Perdida",
            2: "Cripta dos Ecos Temporais",
            3: "Fortaleza do Gelo Eterno",
            4: "Templo da Fenda Temporal",
            5: "Torre dos Algoritmos Perdidos",
            6: "Salões do Caos de Código",
            7: "Lagoa do Loop Infinito",
            8: "Pântano da Lógica Desfeita",
            9: "Ruínas do Depurador Sombrio",
            10: "Câmara da Máquina do Tempo"
        }
        return nomes.get(numero, f"Masmorra {numero}")

    def criarMasmorraAtual(self):
        # Cada masmorra define os próximos caminhos que o jogador pode seguir.
        # A estrutura segue um percurso linear, com ramificações até à masmorra final.
        if self.__masmorraAtual == 1:
            return Masmorra(
                1,
                "Masmorra da Floresta Perdida",
                "Uma floresta húmida onde até as árvores parecem julgar as tuas escolhas. À saída, dois caminhos se abrem: um conduz à Cripta e outro à Fortaleza.",
                caminhosDisponiveis=[2, 3]
            )

        elif self.__masmorraAtual == 2:
            return Masmorra(
                2,
                "Cripta dos Ecos Temporais",
                "Uma cripta onde se ouvem vozes do passado, do futuro e de alunos a perguntar se isto sai no teste. Podes seguir para a Fortaleza ou adentrar o Templo.",
                caminhosDisponiveis=[3, 4]
            )

        elif self.__masmorraAtual == 3:
            return Masmorra(
                3,
                "Fortaleza do Gelo Eterno",
                "Uma fortaleza gelada. O frio é tanto que até os bugs congelam. Dois portões magicos prometem levar-te ao Templo ou à Torre.",
                caminhosDisponiveis=[4, 5]
            )

        elif self.__masmorraAtual == 4:
            return Masmorra(
                4,
                "Templo da Fenda Temporal",
                "Um templo instável onde ontem, hoje e amanhã discutem quando é que se assinam as folhas. Pode seguir para a Torre ou para o Salão do Caos.",
                caminhosDisponiveis=[5, 6]
            )

        elif self.__masmorraAtual == 5:
            return Masmorra(
                5,
                "Torre dos Algoritmos Perdidos",
                "Uma torre onde os cálculos dão voltas e as fórmulas gritam por café. Dois elevadores quebrados levam-te ao Salão do Caos ou à Lagoa.",
                caminhosDisponiveis=[6, 7]
            )

        elif self.__masmorraAtual == 6:
            return Masmorra(
                6,
                "Salões do Caos de Código",
                "Uma sala cheia de gargalhadas de programadores fantasmas e bugs que dançam no teto. De aqui podes furar o Pântano ou seguir para a Lagoa.",
                caminhosDisponiveis=[7, 8]
            )

        elif self.__masmorraAtual == 7:
            return Masmorra(
                7,
                "Lagoa do Loop Infinito",
                "Águas calmas, mas cuidado: alguém pode puxar-te para repetir a mesma linha para sempre. Os dois trilhos seguintes levam-te ao Pântano ou às Ruínas.",
                caminhosDisponiveis=[8, 9]
            )

        elif self.__masmorraAtual == 8:
            return Masmorra(
                8,
                "Pântano da Lógica Desfeita",
                "Um pântano onde as condições nunca se cumprem e até as variáveis andam perdidas. O caminho final está à vista: Ruínas e Câmara do Tempo.",
                caminhosDisponiveis=[9, 10]
            )

        elif self.__masmorraAtual == 9:
            return Masmorra(
                9,
                "Ruínas do Depurador Sombrio",
                "Ruínas antigas onde os erros do passado ainda inexistecem. Só resta um passo final: entrar na Câmara da Máquina do Tempo.",
                caminhosDisponiveis=[10]
            )

        else:
            return Masmorra(
                10,
                "Câmara da Máquina do Tempo",
                "A última masmorra. A máquina está perto. O Wi-Fi ainda não. Não há mais caminhos: só resta vencer o Guardião e regressar.",
                caminhosDisponiveis=[]
            )

    def criarInimigoDaMasmorra(self):
        # Cada masmorra tem um inimigo próprio para aumentar a progressão e a variedade do jogo.
        if self.__masmorraAtual == 1:
            return Inimigo("Gervásio, o morcão", 30, 7, 2, 20, 15)

        elif self.__masmorraAtual == 2:
            return Inimigo("Kled, o guerreiro", 45, 10, 4, 30, 25)

        elif self.__masmorraAtual == 3:
            return Inimigo("Thresh, o carrasco", 65, 13, 6, 45, 35)

        elif self.__masmorraAtual == 4:
            return Inimigo("Jinx, a malvada", 85, 17, 8, 60, 50)

        elif self.__masmorraAtual == 5:
            return Inimigo("Dr. Mundo, o médico", 100, 20, 10, 80, 65)

        elif self.__masmorraAtual == 6:
            return Inimigo("Vex, a aparição de código", 115, 22, 11, 95, 75)

        elif self.__masmorraAtual == 7:
            return Inimigo("Maokai, o guardião", 125, 24, 12, 105, 85)

        elif self.__masmorraAtual == 8:
            return Inimigo("Draven, o cavaleiro", 135, 26, 13, 110, 90)

        elif self.__masmorraAtual == 9:
            return Inimigo("Darius, o senhor da guerra", 150, 28, 14, 120, 100)

        else:
            return Inimigo("Guardião Temporal", 180, 32, 16, 150, 120)

    def explorarMasmorra(self):
        # Cria a masmorra atual e o inimigo correspondente para iniciar a exploração.
        masmorra = self.criarMasmorraAtual()
        self.__inimigoAtual = self.criarInimigoDaMasmorra()

        masmorra.mostrarInformacao()
        masmorra.mostrarCaminhosDisponiveis()

        print("\nAo entrares, sentes uma energia estranha no ar.")
        print("O teu relógio futurista mostra a seguinte mensagem:")
        print('"Erro 1272: realidade medieval não suportada."')

        print("\nUm inimigo apareceu!")
        print("Inimigo:", self.__inimigoAtual.getNome())

        self.iniciarCombate()

    def iniciarCombate(self):
        # Ciclo principal do combate até o jogador ou o inimigo ficar sem vida.
        while self.__jogador.getVida() > 0 and self.__inimigoAtual.getVida() > 0:
            input("[Prima enter para continuar]")
            Recursos.limparConsola()
            print("\n===== COMBATE =====")

            self.__jogador.mostrarEstadoResumido()
            print()
            self.__inimigoAtual.mostrarEstado()
            print()
            print("1. Atacar")
            print("2. Usar poção")
            print("3. Usar consumível de combate")
            print("4. Fugir")

            try:
                opcaoCombate = int(input("Opção: "))
            except ValueError:
                opcaoCombate = 0

            print()
            if opcaoCombate == 1:
                self.__jogador.atacar(self.__inimigoAtual)
            elif opcaoCombate == 2:
                self.__jogador.usarPocao()
            elif opcaoCombate == 3:
                danoConsumivel = self.__jogador.usarConsumivelCombate()
                if danoConsumivel > 0:
                    self.__inimigoAtual.receberDano(danoConsumivel)
            elif opcaoCombate == 4:
                print(f"{self.__inimigoAtual.getNome()} meteu-te demasiado medo. Escolheste dar uma corridinha...")
                input("[Prima enter para continuar]")
                return
            else:
                print("Opção inválida. Perdes a tua vez.")

            if self.__inimigoAtual.getVida() <= 0:
                break

            if self.__jogador.getVida() > 0:
                self.__inimigoAtual.atacar(self.__jogador)

        if self.__jogador.getVida() <= 0:
            self.processarDerrota()
        else:
            self.processarVitoria()

    def processarVitoria(self):
        print(f"Ganhaste o combate contra o {self.__inimigoAtual.getNome()}")
        self.__jogador.ganharExperiencia(self.__inimigoAtual.getExperiencia())
        self.__jogador.ganharMoedas(self.__inimigoAtual.getMoedas())

        # Permitir ao jogador escolher para qual masmorra seguir,
        # com base nos caminhos disponíveis da masmorra atual.
        self.escolherCaminhoAposVitoria()
        input("[Prima enter para continuar]")

    def escolherCaminhoAposVitoria(self):
        # Permite ao jogador escolher qual será a próxima masmorra após vencer o combate atual.
        masmorra = self.criarMasmorraAtual()
        caminhos = masmorra.getCaminhosDisponiveis()

        if not caminhos:
            # Se não houver caminhos (ex: masmorra final), avançar ou terminar.
            if self.__masmorraAtual == 10:
                self.fimDoJogo()
            else:
                self.avancarMasmorra()
            return

        print("\nEscolhe para onde seguir:")
        for idx, destino in enumerate(caminhos, start=1):
            nomeDestino = self.obterNomeMasmorra(destino)
            print(f"{idx} - Ir para {nomeDestino}")
        print("0 - Permanecer nesta masmorra")

        while True:
            escolha = input("Escolha: ")
            if escolha == "0":
                print("Permanences na mesma masmorra para explorar mais tarde.")
                return
            if not escolha.isdigit():
                print("Opção inválida. Insere um número.")
                continue

            indice = int(escolha) - 1
            if indice < 0 or indice >= len(caminhos):
                print("Opção inválida. Escolhe uma das opções listadas.")
                continue

            destino = caminhos[indice]
            print(f"Segues para a masmorra {destino}.")
            self.__masmorraAtual = destino
            return

    def processarDerrota(self):
        # Quando o jogador perde, o jogo termina e a aventura acaba.
        print(f"{self.__jogador.getNome()} foi derrotado(a).")
        print("A máquina do tempo ficou mais longe do que nunca.")
        self.__terminado = True
        input("[Prima enter para continuar]")

    def avancarMasmorra(self):
        if self.__masmorraAtual == 10:
            self.fimDoJogo()
        else:
            self.__masmorraAtual += 1

    def visitarLoja(self):
        self.__loja.gerarProdutos(self.__masmorraAtual)
        self.__loja.mostrarProdutos()

        while True:
            print("\nEscolha o número do item para comprar ou 0 para sair.")
            escolha = input("Escolha: ")

            if escolha == "0":
                print("\nSaíste da loja.")
                print("O ferreiro grita: 'Volta sempre! E traz moedas, não aceitamos MB Way!'")
                input("[Prima enter para continuar]")
                return

            if not escolha.isdigit():
                print("Opção inválida. Insere um número válido.")
                continue

            indice = int(escolha) - 1
            self.__loja.comprarProduto(indice, self.__jogador)
            input("[Prima enter para continuar]")
            return

    def descansar(self):
        # O descanso recupera vida, mas tem um número limitado de usos.
        if self.__descansosRestantes <= 0:
            print("\nJá usaste todos os descansos disponíveis. Não podes descansar mais.")
            input("[Prima enter para continuar]")
            return

        valorRecuperacao = 25
        self.__jogador.curar(valorRecuperacao)
        self.__descansosRestantes -= 1
        print(f"\nDescansaste por um momento e recuperaste {valorRecuperacao} pontos de vida.")
        print(f"Descansos restantes: {self.__descansosRestantes}")
        print("O silêncio da noite medieval não é tão mau, desde que não sejas atacado.")
        input("[Prima enter para continuar]")

    def fimDoJogo(self):
        if self.__jogador.getVida() <= 0:
            # fim do jogo por derrota
            print(f"{self.__jogador.getNome()} caiu... Voltar para o presente terá de ficar para outra vida...")
            print("Não foste forte suficiente para superar este desafio")
        else:
            # fim do jogo com vitoria
            print("Parabéns! Recuperaste o núcleo temporal e voltaste ao ano 2077.")

        self.__terminado = True
        return self.__terminado
