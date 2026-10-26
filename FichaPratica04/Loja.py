import random

try:
    from .Arma import Arma
    from .Armadura import Armadura
    from .Pocao import Pocao
    from .ConsumivelCombate import ConsumivelCombate
except ImportError:
    from Arma import Arma
    from Armadura import Armadura
    from Pocao import Pocao
    from ConsumivelCombate import ConsumivelCombate


class Loja:
    # Responsável por criar, mostrar e vender os produtos disponíveis ao jogador.
    def __init__(self):
        self.__produtosDisponiveis = []

    def getProdutosDisponiveis(self):
        return self.__produtosDisponiveis

    def gerarProdutos(self, numeroMasmorra):
        # Cria a lista de produtos que aparecem na loja conforme a masmorra atual.
        produtos = []

        if numeroMasmorra == 1:
            produtos.extend([
                Arma("Espada de Madeira", 3, 20),
                Arma("Machado Oxidado", 4, 25),
                Armadura("Colete de Linho", 2, 18),
                Armadura("Cota de Couro", 3, 24),
                Pocao("Poção de Cura Básica", 20, 10),
                Pocao("Poção de Regeneração", 25, 12),
                ConsumivelCombate("Besta Rústica", 8, 12, 15),
                ConsumivelCombate("Flecha Flamejante", 10, 14, 18),
                ConsumivelCombate("Granada de Fumaça", 6, 10, 12),
                ConsumivelCombate("Soco Tóxico", 9, 13, 17),
            ])
        elif numeroMasmorra == 2:
            produtos.extend([
                Arma("Espada de Ferro", 6, 45),
                Arma("Lança de Bronze", 7, 50),
                Armadura("Armadura de Couro", 4, 40),
                Armadura("Escudo Pesado", 5, 48),
                Pocao("Poção de Cura Média", 35, 25),
                Pocao("Poção de Vigor", 40, 28),
                ConsumivelCombate("Bomba de Chama", 12, 18, 30),
                ConsumivelCombate("Dardo Explosivo", 14, 20, 35),
                ConsumivelCombate("Poção de Veneno", 10, 16, 25),
                ConsumivelCombate("Tempestade de Fogo", 15, 22, 38),
            ])
        elif numeroMasmorra == 3:
            produtos.extend([
                Arma("Lança de Guerra", 9, 75),
                Arma("Espada Curvada", 10, 82),
                Armadura("Armadura de Ferro", 7, 70),
                Armadura("Cota de Malha", 8, 76),
                Pocao("Poção de Cura Forte", 50, 40),
                Pocao("Elixir da Resistência", 55, 42),
                ConsumivelCombate("Garra de Gelo", 18, 26, 55),
                ConsumivelCombate("Shuriken Arcana", 16, 24, 50),
                ConsumivelCombate("Corrente Elétrica", 17, 25, 53),
                ConsumivelCombate("Orbe Explosiva", 19, 28, 60),
            ])
        elif numeroMasmorra == 4:
            produtos.extend([
                Arma("Espada Lendária", 13, 110),
                Arma("Martelo Ancestral", 14, 118),
                Armadura("Armadura de Aço", 10, 100),
                Armadura("Peitoral Rúnico", 11, 108),
                Pocao("Poção de Cura Superior", 70, 60),
                Pocao("Poção da Vitalidade", 75, 65),
                ConsumivelCombate("Flecha de Relâmpago", 22, 30, 78),
                ConsumivelCombate("Bomba de Gelo", 20, 28, 72),
                ConsumivelCombate("Sopro de Dragão", 23, 32, 85),
                ConsumivelCombate("Aura de Fúria", 24, 34, 88),
            ])
        else:
            produtos.extend([
                Arma("Excalibur Temporal", 18, 160),
                Arma("Lâmina Dimensional", 20, 170),
                Armadura("Armadura do Núcleo", 15, 150),
                Armadura("Cota Temporal", 16, 158),
                Pocao("Poção do Tempo", 100, 90),
                Pocao("Elixir do Núcleo", 110, 98),
                ConsumivelCombate("Orbe Temporal", 28, 40, 110),
                ConsumivelCombate("Runa Destruidora", 26, 38, 108),
                ConsumivelCombate("Campo de Força", 25, 36, 105),
                ConsumivelCombate("Estilhaço de Éter", 27, 39, 112),
            ])

        self.__produtosDisponiveis = random.sample(produtos, min(10, len(produtos)))

    def mostrarProdutos(self):
        # Mostra os itens disponíveis para compra ao jogador.
        print("===== LOJA DO FERREIRO =====")
        print("O ferreiro olha para ti e diz:")
        print('"Não sei o que é um carregador USB-C, mas tenho espadas e outras coisas."')

        if len(self.__produtosDisponiveis) == 0:
            print("Nenhum produto disponível.")
            return

        for index, produto in enumerate(self.__produtosDisponiveis, start=1):
            print(f"{index} - {self._tipoProduto(produto)}")
            produto.mostrarDados()

        print("0 - Sair da loja")

    def _tipoProduto(self, produto):
        # Identifica o tipo de produto para mostrar uma descrição correta na loja.
        if isinstance(produto, Arma):
            return "Arma"
        if isinstance(produto, Armadura):
            return "Armadura"
        if isinstance(produto, Pocao):
            return "Poção"
        if isinstance(produto, ConsumivelCombate):
            return "Consumível de combate"
        return "Item desconhecido"

    def comprarProduto(self, indice, jogador):
        # Processa a compra de um item e atualiza o estado do jogador.
        if indice < 0 or indice >= len(self.__produtosDisponiveis):
            print("Seleção inválida.")
            return

        produto = self.__produtosDisponiveis[indice]
        preco = produto.getPreco()

        if isinstance(produto, (Pocao, ConsumivelCombate)) and jogador.getTotalItensInventario() >= jogador.getLimiteInventario():
            print("O teu inventário está cheio. Não consegues comprar este item.")
            return

        if not jogador.gastarMoedas(preco):
            print("Não tens moedas suficientes para comprar este item.")
            return

        if isinstance(produto, Arma):
            jogador.equiparArma(produto)
            print(f"Compraste {produto.getNome()} e equipaste a arma.")
        elif isinstance(produto, Armadura):
            jogador.equiparArmadura(produto)
            print(f"Compraste {produto.getNome()} e equipaste a armadura.")
        elif isinstance(produto, Pocao):
            if not jogador.guardarPocao(produto):
                jogador.ganharMoedas(preco)
                return
            print(f"Compraste {produto.getNome()} e guardaste a poção no inventário.")
        elif isinstance(produto, ConsumivelCombate):
            if not jogador.adicionarConsumivelCombate(produto):
                jogador.ganharMoedas(preco)
                return
            print(f"Compraste {produto.getNome()} e guardaste-o no inventário de combate.")
        else:
            print("Item desconhecido. Compra não efetuada.")
            jogador.ganharMoedas(preco)
            return

        self.__produtosDisponiveis.pop(indice)
