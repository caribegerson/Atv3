from Menu import Menu
from UserInterface import UserInterface
from MenuRepository import MenuRepository
from Order import Order


def test_get_user_input():
    # Arrange
    repositorio = MenuRepository()
    interface = UserInterface(repositorio)
    ordem_comparacao = Order(1, 5)
    
    # Act
    ordem_teste = interface.get_user_input()

    # Assert
    assert ordem_teste.code == ordem_comparacao.code
    assert ordem_teste.quantity == ordem_comparacao.quantity

def test_get_total_price():
    # Arrange
    repositorio = MenuRepository()
    menu = Menu(1, "Teste 1", 5)
    interface = UserInterface(repositorio)
    ordem_preco = Order(1, 5)
    
    # Act
    repositorio.set_menu_item(menu)
    resultado = interface.get_total_price(ordem_preco)

    # Assert
    assert resultado == 25

