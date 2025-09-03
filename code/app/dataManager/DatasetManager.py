import pandas as pd
from typing import List, Dict

from bloons.Bloon import Bloon

class DatasetManager:
    def __init__(self, caminho_csv: str):
        self.caminho_csv = caminho_csv
        self.baloes: Dict[str, Bloon] = {}

    def carregar_dataset(self):
        self.baloes.clear()
        df = pd.read_csv(self.caminho_csv)
        for _, linha in df.iterrows():
            nome = linha['nome']
            vida_base = int(linha['vida_base'])
            velocidade = float(linha['velocidade'])

            imunidades = [i.strip() for i in str(linha['imunidades']).split(',') if i.strip() and i.strip().lower() != "nenhuma"]
            filhos = {}
            if str(linha['filhos']).strip().lower() != "nenhum":
                for f in str(linha['filhos']).split(','):
                    qtd, filho_nome = f.strip().split('x')
                    filhos[filho_nome.strip()] = int(qtd.strip())

            bloon = Bloon(nome, vida_base, velocidade, imunidades, filhos)
            self.baloes[nome.lower()] = bloon

    def buscar_bloon(self, nome: str) -> Bloon:
        return self.baloes.get(nome.lower())

    def listar_baloes(self) -> List[str]:
        return list(self.baloes.keys())