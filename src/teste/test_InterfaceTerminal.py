import pytest
from unittest.mock import Mock
from io import StringIO

from app.dataManager.DatasetManager import DatasetManager
from app.frontEnd.InterfaceTerminal import InterfaceTerminal

@pytest.fixture
def mock_dataset_manager():
    # cria um mock do DatasetManager
    return Mock(spec=DatasetManager)


@pytest.fixture
def interface(mock_dataset_manager):
    # cria uma instância da InterfaceTerminal com o mock
    return InterfaceTerminal(mock_dataset_manager)


def test_listar_baloes_com_sucesso(interface, mock_dataset_manager, capsys):
    baloes_falsos = ['red', 'blue', 'green']
    mock_dataset_manager.listar_baloes.return_value = baloes_falsos

    # testando método
    interface.listar_baloes()

    captured = capsys.readouterr()
    output = captured.out

    mock_dataset_manager.listar_baloes.assert_called_once()

    assert "- Red" in output
    assert "- Blue" in output
    assert "- Green" in output
    assert "Lista de Balões Disponíveis" in output


def test_buscar_bloon_encontrado(interface, mock_dataset_manager, monkeypatch, capsys):
    info_bloon_falso = "Nome: Red Bloon, RBE: 1"
    mock_dataset_manager.buscar_bloon.return_value = info_bloon_falso

    # Simula a entrada do usuário ("Red")
    monkeypatch.setattr('builtins.input', lambda _: 'Red')

    interface.buscar_bloon()

    captured = capsys.readouterr()
    output = captured.out

    mock_dataset_manager.buscar_bloon.assert_called_once_with('red')

    assert info_bloon_falso in output


def test_buscar_bloon_nao_encontrado(interface, mock_dataset_manager, monkeypatch, capsys):
    # Configura o mock para retornar Null, ou seja um balão não encontrado
    mock_dataset_manager.buscar_bloon.return_value = None

    # Simula a entrada do usuário
    monkeypatch.setattr('builtins.input', lambda _: 'Purple')

    interface.buscar_bloon()
    
    captured = capsys.readouterr()
    output = captured.out

    mock_dataset_manager.buscar_bloon.assert_called_once_with('purple')

    assert "Balão não encontrado!" in output


def test_menu_invoca_listar_baloes_do_manager_na_opcao_1(interface, monkeypatch, mock_dataset_manager):
    mock_dataset_manager.listar_baloes.return_value = [] 
    
    # Simula o usuário digitando '1' e depois '3' para sair do loop
    user_input_string = '1\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input_string))

    interface.menu()

    mock_dataset_manager.listar_baloes.assert_called_once()


def test_menu_invoca_buscar_bloon_do_manager_na_opcao_2(interface, monkeypatch, mock_dataset_manager):
    mock_dataset_manager.buscar_bloon.return_value = "Info do Balão"
    
    # Simula o usuário digitando '2', em seguida o nome 'red', e depois '3' para sair
    user_input_string = '2\nred\n3\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input_string))
    
    interface.menu()

    mock_dataset_manager.buscar_bloon.assert_called_once_with('red')


def test_menu_exibe_mensagem_para_opcao_invalida(interface, monkeypatch, capsys):
    # Simula o usuário digitando uma opção inválida ('9') e depois '3' para sair
    user_inputs = iter(['9', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))

    interface.menu()

    captured = capsys.readouterr()
    output = captured.out

    assert "Opção inválida!" in output


def test_menu_sai_na_opcao_3(interface, monkeypatch, capsys):
    # Simula o usuário digitando '3'
    monkeypatch.setattr('builtins.input', lambda _: '3')

    interface.menu()

    captured = capsys.readouterr()
    output = captured.out

    assert "Saindo da DataBase..." in output