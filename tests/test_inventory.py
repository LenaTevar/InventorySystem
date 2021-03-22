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
    # Test basic empty inventory data 
    assert empty_inventory.max_weight == 100
    assert empty_inventory.max_size == 25
    assert empty_inventory.current_cash == 0
    assert len(empty_inventory.items_list) == 0
    assert empty_inventory.remaining_weight() == empty_inventory.max_weight
    assert empty_inventory.current_weight() == 0

def test_inventory_pickup():  
    # Test pick up one item
    empty_inventory = Inventory()
    item_small =  Item(name="Test item", weight=1, value=1)

    assert empty_inventory.pickup(item_small)

    # Test inventory full
    for x in range(24):
        empty_inventory.pickup(item_small)
    assert empty_inventory.get_totalnr_items() == 25

    assert empty_inventory.current_weight() == 25
    assert not empty_inventory._itemlist_freespace()

    with pytest.raises(InvalidQuantityException, match=r"Inventory full") as ex: 
        empty_inventory.pickup(item_small)  
        
def test_inventory_typeError(empty_inventory):
    # Test no params exception
    with pytest.raises(TypeError):
        empty_inventory.pickup()

def test_inventory_drop(empty_inventory, item_weapon, heavy_item):
    # Test drop item and try to drop item not owned
    empty_inventory.pickup(item_weapon)
    assert empty_inventory.drop(item_weapon)
    assert not empty_inventory.drop(heavy_item)


def test_inventory_weight(empty_inventory, item_weapon, medium_item):
    # Test weight of the inventory
    expected_total_weight = 0
    
    assert empty_inventory.weight_by_type(Item_Type.Consumable) == 0

    empty_inventory.pickup(item_weapon)
    empty_inventory.pickup(medium_item)
    expected_total_weight = item_weapon.weight + medium_item.weight

    assert empty_inventory.remaining_weight() == empty_inventory.max_weight - expected_total_weight
    assert empty_inventory.current_weight() == expected_total_weight
    assert empty_inventory.weight_by_type(Item_Type.Consumable) == 20

def test_inventory_pickup_weight(empty_inventory, item_weapon, heavy_item): 
    # Test weight limit exception

    empty_inventory.pickup(heavy_item)
    assert empty_inventory.current_weight() == heavy_item.weight

    with pytest.raises(InvalidQuantityException, match=r"Weight full") as ex: 
        empty_inventory.pickup(heavy_item) 