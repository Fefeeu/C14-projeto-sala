from dataManager.DatasetManager import DatasetManager

class InterfaceTerminal:
    def __init__(self, dataset_manager: DatasetManager):
        self.dataset_manager = dataset_manager

    def menu(self):
        while True:
            print("\n=== BTD6 Pokedex ===")
            print("1. Listar todos os balões")
            print("2. Buscar informações de um balão")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.listar_baloes()
            elif opcao == '2':
                self.buscar_bloon()
            elif opcao == '3':
                print("Saindo da Pokedex...")
                break
            else:
                print("Opção inválida!")

    def listar_baloes(self):
        print("\nLista de Balões Disponíveis:")
        for nome in self.dataset_manager.listar_baloes():
            print(f"- {nome.title()}")

    def buscar_bloon(self):
        nome = input("Digite o nome do balão: ")
        bloon = self.dataset_manager.buscar_bloon(nome.lower())
        if bloon:
            print(bloon)
        else:
            print("Balão não encontrado!")