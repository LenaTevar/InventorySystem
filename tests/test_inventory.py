from InventorySystem.src.Inventory import Inventory
from InventorySystem.src.Item import Item
from InventorySystem.src.Items_Types import Item_Type
import pytest
##########################################################
#
#   FIXTURES
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
    return Item(name="Test item", weight=1, value=1)

@pytest.fixture
def heavy_item():
    return Item(name="Heavy item", weight=99, value=99, itype=Item_Type.Gear)

##########################################################
#
#   INVENTORY TESTS
#
##########################################################
def test_inventory(empty_inventory):    
    assert empty_inventory.max_weight == 100
    assert empty_inventory.max_size == 25

def test_inventory_pickup(empty_inventory, item_weapon):    
    assert empty_inventory.pickup(item_weapon)

    for x in range(24):
        empty_inventory.pickup(item_weapon)
    
    try:
        empty_inventory.pickup(item_weapon)
    except InvalidQuantityException as ex:
        assert isinstance(ex, type(Exception))
        assert ex.args == "Space exceeded"


def test_inventory_drop(empty_inventory, item_weapon): 
    assert empty_inventory.drop(item_weapon)
    pass

def test_inventory_item_get_sort():
    #get items by type
    #sort items by type
    #sort items by value
    #sort items by weight
    #free item slots
    #total number of items
    pass
def test_inventory_weight():
    #get remaining weight
    #current weight
    #get weight by tipe of item
    pass 
def test_inventory_cash():
    #sell item
    #buy item
    #pickup cash
    pass 
