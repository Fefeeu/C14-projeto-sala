import pytest
import io
from app.dataManager.DatasetManager import DatasetManager
# MUDANDO LINHA PARA DAR PUSH E TESTAR O PIPELINE 6
#1 invalido
def test_carregar_dataset_com_caminho_invalido():

    df = DatasetManager("caminho/que/nao/existe/arquivo.csv")
    
    with pytest.raises(FileNotFoundError):
        df.carregar_dataset()

    # Garantindo que a lista de balões continua vazia após a falha
    assert len(df.baloes) == 0

#1 valido
def test_carregar_dataset_com_arquivo_valido():
    csv_data = """nome,vida_base,velocidade,imunidades,filhos
vermelho,1,1.0,Nenhuma,2x Amarelo
azul,2,1.2,Nenhuma,2x Vermelho
"""
    
    caminho_arquivo_falso = io.StringIO(csv_data)
    
    df = DatasetManager(caminho_arquivo_falso)
    df.carregar_dataset()
    
    assert len(df.baloes) == 2
    assert "vermelho" in df.baloes
    assert df.baloes["vermelho"].vida_base == 1
    assert df.baloes["vermelho"].velocidade == 1.0
    assert df.baloes["vermelho"].imunidades == [] 
    
#2 invalido
def test_carregar_dataset_com_csv_vazio():
    csv_data = "nome,vida_base,velocidade,imunidades,filhos\n" # Apenas o cabeçalho
    caminho_flaso = io.StringIO(csv_data)
    df = DatasetManager(caminho_flaso)
    df.carregar_dataset()
    
    assert len(df.baloes) == 0

#3 invalido
def test_carregar_dataset_com_coluna_faltando():
    csv_data = """nome,vida_base,imunidades,filhos
vermelho,1,Nenhuma,Nenhum\n"""
    caminho_fake = io.StringIO(csv_data)
    df = DatasetManager(caminho_fake)
    
    with pytest.raises(KeyError):
        df.carregar_dataset()

#4 invalido
def test_carregar_dataset_com_vida_nao_numerica():
    csv_data = """nome,vida_base,velocidade,imunidades,filhos
vermelho,dez,1.0,Nenhuma,Nenhum\n"""
    
    caminho_flaso = io.StringIO(csv_data)
    df = DatasetManager(caminho_flaso)
    
    with pytest.raises(ValueError):
        df.carregar_dataset()

#2 valido
def test_sobreescrever_dataset():
    csv_data1 = """nome,vida_base,velocidade,imunidades,filhos
vermelho,1,1.0,Nenhuma,Nenhum\n"""
    
    csv_data2 = """nome,vida_base,velocidade,imunidades,filhos
azul,2,1.2,Nenhuma,Nenhum\n"""
    
    df = DatasetManager(io.StringIO(csv_data1))
    df.carregar_dataset()
    
    assert len(df.baloes) == 1
    assert "vermelho" in df.baloes
    
    df.caminho_csv = io.StringIO(csv_data2)
    df.carregar_dataset()
    
    assert len(df.baloes) == 1
    assert "azul" in df.baloes
    assert "vermelho" not in df.baloes

#5 invalido
def test_buscar_bloon_nao_existente():
    df = DatasetManager("auxiliar/balloons.csv")
    df.carregar_dataset()
    
    bloon = df.buscar_bloon("balão não existente")
    
    assert bloon is None

#3 valido
def test_buscar_bloon_existente():
    df = DatasetManager("auxiliar/balloons.csv")
    df.carregar_dataset()
    
    bloon = df.buscar_bloon("Red Bloon")
    
    assert bloon is not None
    assert bloon.nome == "Red Bloon"

#4 valido
def test_buscar_bloon_com_case_diferentes():
    csv_data = """nome,vida_base,velocidade,imunidades,filhos
Red Bloon,1,1.0,Nenhuma,Nenhum\n"""
    
    df = DatasetManager(io.StringIO(csv_data))
    df.carregar_dataset()
    
    bloon1 = df.buscar_bloon("Red Bloon")
    bloon2 = df.buscar_bloon("red bloon")
    bloon3 = df.buscar_bloon("RED BLOON")
    
    assert bloon1 is not None
    assert bloon1 is bloon2  # Verifica se é o mesmo objeto
    assert bloon2 is bloon3  # Verifica se é o mesmo objeto

#6 invalido    
def test_buscar_bloon_tipo_nao_string():
    csv_data = "nome,vida_base,velocidade,imunidades,filhos\nRed Bloon,1,1.0,Nenhuma,Nenhum\n"
    df = DatasetManager(io.StringIO(csv_data))
    df.carregar_dataset()
    
    with pytest.raises(AttributeError):
        df.buscar_bloon(12345)  # Passando um inteiro em vez de string


#7 invalido
def test_listar_baloes_antes_de_carregar_dataset():
    df = DatasetManager("caminho_qualquer.csv")
    
    assert df.listar_baloes() == []

#5 valido
def test_verificar_convercao_imunidades():
    csv_data = """nome,vida_base,velocidade,imunidades,filhos
vermelho,1,1.0,Nenhuma,Nenhum
azul,2,1.2,Fogo,2x Gelo
"""
    
    caminho_arquivo_falso = io.StringIO(csv_data)
    
    df = DatasetManager(caminho_arquivo_falso)
    df.carregar_dataset()
    
    assert df.baloes["vermelho"].imunidades == []
    assert df.baloes["azul"].imunidades == ["Fogo"]
 
#6 valido   
def test_verificar_convercao_filhos():
    csv_data = """nome,vida_base,velocidade,imunidades,filhos
vermelho,1,1.0,Nenhuma,Nenhum
azul,2,1.2,Nenhuma,2x Vermelho
"""
    
    caminho_arquivo_falso = io.StringIO(csv_data)
    
    df = DatasetManager(caminho_arquivo_falso)
    df.carregar_dataset()
    
    assert df.baloes["vermelho"].filhos == {}
    assert df.baloes["azul"].filhos == {"Vermelho": 2}

#13 no total 
