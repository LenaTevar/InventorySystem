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


def test_inventory_item_get_sort(loaded_inventory,list_of_items):
    # Test lenght of the inventory
    expected_total = len(list_of_items)
    resulted_total = loaded_inventory.get_totalnr_items()
    assert expected_total == resulted_total

    # Test free space left in the inventory
    expected_feesize_total = loaded_inventory.max_size - len(list_of_items)
    resulted_feesize_total = loaded_inventory.get_free_space()
    assert expected_feesize_total == resulted_feesize_total

    # Test get inventory by type of item
    expected_by_type = [item for item in  list_of_items if item.type == Item_Type.Weapon]
    resulted_by_type = loaded_inventory.get_items_by_type(Item_Type.Weapon)
    assert expected_by_type == resulted_by_type
    
    # Test get inventory sorted by value of the items
    expected_sorted_by_value = sorted(list_of_items, key=lambda item: item.value)
    resulted_sorted_by_value = loaded_inventory.items_sort_value()
    assert expected_sorted_by_value == resulted_sorted_by_value

    # Test get inventory sorted by weight of the items
    expected_sorted_by_weight = sorted(list_of_items, key=lambda item: item.weight)
    resulted_sorted_by_weight = loaded_inventory.items_sort_weight()
    assert expected_sorted_by_weight == resulted_sorted_by_weight
