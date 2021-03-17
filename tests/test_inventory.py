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
def test_inventory(empty_inventory):    
    assert empty_inventory.max_weight == 100
    assert empty_inventory.max_size == 25

def test_inventory_pickup(empty_inventory, item_weapon, heavy_item):    
    assert empty_inventory.pickup(item_weapon)

    for x in range(24):
        empty_inventory.pickup(item_weapon)
    
    try:
        empty_inventory.pickup(item_weapon)
    except InvalidQuantityException as ex:
        assert isinstance(ex, type(Exception))
        assert ex.args == "Space exceeded"

    try:
        empty_inventory.pickup(heavy_item)
    except InvalidQuantityException as ex:
        assert isinstance(ex, type(Exception))
        assert ex.args == "Weigth exceeded"

def test_inventory_typeError(empty_inventory):
    with pytest.raises(TypeError):
        empty_inventory.pickup()



def test_inventory_drop(empty_inventory, item_weapon, heavy_item):
    empty_inventory.pickup(item_weapon)
    assert empty_inventory.drop(item_weapon)
    assert not empty_inventory.drop(heavy_item)

def test_inventory_item_get_sort():
    #get items by type
    #sort items by type
    #sort items by value
    #sort items by weight
    #free item slots
    #total number of items
    pass
def test_inventory_weight(empty_inventory, item_weapon, medium_item):
    empty_inventory.pickup(item_weapon)
    empty_inventory.pickup(medium_item)
    expected_total_weight = item_weapon.Weight + medium_item.Weight
    assert empty_inventory.remaining_weight() == empty_inventory.max_weight - expected_total_weight
    assert empty_inventory.current_weight() == expected_total_weight
    assert empty_inventory.weight_by_type(Item_Type.Consumable) == 20

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
    pass 
