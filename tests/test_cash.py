from InventorySystem.src.Inventory import Inventory
from InventorySystem.src.Item import Item
from InventorySystem.src.Items_Types import Item_Type
import pytest 
##########################################################
#
#   FIXTURES
#   Pre-made models used for testing 
#
##########################################################
@pytest.fixture
def empty_inventory():
    """
    Creates an inventory, always the same.
    """
    return Inventory()

@pytest.fixture
def item_weapon():
    """
    Creates an light item weight=1, value=1
    """
    return Item(name="Test item", weight=1, value=1)

@pytest.fixture
def medium_item():
    """
    Creates a medium item weight=20, value=5
    """
    return Item(name="Heavy item", weight=20, value=5, itype=Item_Type.Consumable)

@pytest.fixture
def heavy_item():
    """
    Creates a heavy and expensive item weight=99, value=99
    """
    return Item(name="Heavy item", weight=99, value=99, itype=Item_Type.Gear)
@pytest.fixture
def loaded_inventory():
    """
    Creates an inventory already loaded with items
    """
    inventory = Inventory()
    nokia_phone = Item(name="Nokia Phone", weight=1, value=100, itype=Item_Type.Weapon)
    stick = Item(name="A nice stick", weight=12, value=13, itype=Item_Type.Weapon)
    coffee = Item(name="3 Liters of Coffee", weight=3, value=20, itype=Item_Type.Consumable)
    Ear = Item(name="Enemy's Ear", weight=1, value=1, itype=Item_Type.Consumable)
    silly_hat = Item(name="Silly hat", weight=5, value=34, itype=Item_Type.Gear)
    inventory.pickup(nokia_phone)
    inventory.pickup(coffee)
    inventory.pickup(silly_hat)
    inventory.pickup(stick)
    inventory.pickup(Ear)
    return inventory
@pytest.fixture
def list_of_items():
    nokia_phone = Item(name="Nokia Phone", weight=1, value=100, itype=Item_Type.Weapon)
    stick = Item(name="A nice stick", weight=12, value=13, itype=Item_Type.Weapon)
    coffee = Item(name="3 Liters of Coffee", weight=3, value=20, itype=Item_Type.Consumable)
    Ear = Item(name="Enemy's Ear", weight=1, value=1, itype=Item_Type.Consumable)
    silly_hat = Item(name="Silly hat", weight=5, value=34, itype=Item_Type.Gear)
    return [nokia_phone,stick,coffee,Ear,silly_hat]
##########################################################
#
#   INVENTORY TESTS
#
##########################################################


def test_inventory_cash(empty_inventory, item_weapon, medium_item, heavy_item):
    empty_inventory.pickup(item_weapon)
    empty_inventory.pickup(medium_item)
    empty_inventory.pickup(heavy_item)

    # Simple sell
    assert empty_inventory.sell(heavy_item)
    assert empty_inventory.current_cash == 99

    # Simple buy
    assert empty_inventory.buy(heavy_item)
    assert empty_inventory.current_cash == 0

    #Not enough money
    try:
        empty_inventory.buy(heavy_item)
    except InvalidQuantityException as ex:
        assert isinstance(ex, type(Exception))
        assert ex.args == "Not enough money"

    # Simple pickup
    current_money = empty_inventory.current_cash
    empty_inventory.get_cash(100)
    assert empty_inventory.current_cash == current_money + 100

    #Not enough space
    try:
        empty_inventory.buy(item_weapon)
    except InvalidQuantityException as ex:
        assert isinstance(ex, type(Exception))
        assert ex.args == "Space exceeded"
    
