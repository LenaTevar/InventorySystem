from InventorySystem.src.Inventory import Inventory
import pytest

@pytest.fixture
def empty_inventory():
    """
    Creates an inventory, always the same.
    """
    return Inventory()

def test_inventory(empty_inventory):    
    assert empty_inventory.max_weight == 100
    assert empty_inventory.max_size == 25

def test_pickup():
    pass
def test_drop():
    pass
def test_view_items():
    pass
def test_group_items():
    pass
def 