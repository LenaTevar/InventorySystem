from InventorySystem.src.Inventory import Inventory
from InventorySystem.src.Item import Item
from InventorySystem.src.Items_Types import Item_Type
from InventorySystem.src.InvalidQuantityException import InvalidQuantityException
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

##########################################################
#
#   INVENTORY TESTS
#
##########################################################
def test_inventory_cash_buy_sell(empty_inventory, item_weapon, medium_item, heavy_item):
    assert empty_inventory.current_cash == 0

    empty_inventory.pickup(item_weapon)
    empty_inventory.pickup(medium_item)

    # Simple sell
    assert empty_inventory.sell(medium_item)
    assert empty_inventory.current_cash == medium_item.value

    # Simple buy
    assert empty_inventory.buy(medium_item)
    assert empty_inventory.current_cash == 0

def test_inventory_cash_exceptions(empty_inventory, heavy_item):
    with pytest.raises(InvalidQuantityException, match=r"Not enough money") as ex: 
        empty_inventory.buy(heavy_item) 

def test_inventory_typeError(empty_inventory):
    # Test no params exception
    with pytest.raises(TypeError):
        empty_inventory.buy()

    with pytest.raises(TypeError):
        empty_inventory.sell()