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

def test_inventory_item_get_sort(loaded_inventory,list_of_items):
   
    expected_total = len(list_of_items)
    resulted_total = loaded_inventory.get_totalnr_items()
    assert expected_total == resulted_total

    expected_feesize_total = loaded_inventory.max_size - len(list_of_items)
    resulted_feesize_total = loaded_inventory.get_free_space()
    assert expected_feesize_total == resulted_feesize_total

    expected_by_type = [item for item in  list_of_items if item.type == Item_Type.Weapon]
    resulted_by_type = loaded_inventory.get_items_by_type(Item_Type.Weapon)
    assert expected_by_type == resulted_by_type
    

    expected_sorted_by_value = sorted(list_of_items, key=lambda item: item.value)
    resulted_sorted_by_value = loaded_inventory.items_sort_value()
    assert expected_sorted_by_value == resulted_sorted_by_value

    expected_sorted_by_weight = sorted(list_of_items, key=lambda item: item.weight)
    resulted_sorted_by_weight = loaded_inventory.items_sort_weight()
    assert expected_sorted_by_weight == resulted_sorted_by_weight


def test_inventory_weight(empty_inventory, item_weapon, medium_item):
    empty_inventory.pickup(item_weapon)
    empty_inventory.pickup(medium_item)
    expected_total_weight = item_weapon.weight + medium_item.weight

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
    
