from typing import List, Dict

class Bloon:
    def __init__(self, nome: str, vida_base: int, velocidade: float, imunidades: List[str], filhos: Dict[str, int]):
        self._nome = nome
        self._vida_base = vida_base
        self._velocidade = velocidade
        self._imunidades = imunidades
        self._filhos = filhos

    # Encapsulamento com propriedades
    @property
    def nome(self):
        return self._nome

    @property
    def vida_base(self):
        return self._vida_base

    @property
    def velocidade(self):
        return self._velocidade

    @property
    def imunidades(self):
        return self._imunidades

    @property
    def filhos(self):
        return self._filhos

    def __str__(self):
        filhos_str = ", ".join([f"{qtd}x {nome}" for nome, qtd in self._filhos.items()]) if self._filhos else "Nenhum"
        imunidades_str = ", ".join(self._imunidades) if self._imunidades else "Nenhuma"
        return (
            f"\n=== {self._nome} ===\n"
            f"Vida Base: {self._vida_base}\n"
            f"Velocidade: {self._velocidade}\n"
            f"Imunidades: {imunidades_str}\n"
            f"Filhos: {filhos_str}\n"
        )