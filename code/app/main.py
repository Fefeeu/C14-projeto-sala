from dataManager.DatasetManager import DatasetManager
from frontEnd.InterfaceTerninal import InterfaceTerminal

if __name__ == "__main__":
    dataset = DatasetManager("auxiliar/balloons.csv")  # coloque o nome do arquivo CSV salvo
    dataset.carregar_dataset()

    ui = InterfaceTerminal(dataset)
    ui.menu()
