from InventorySystem.src.Inventory import Inventory
from InventorySystem.src.Item import Item
from InventorySystem.src.Items_Types import Item_Type
from InventorySystem.src.InvalidQuantityException import InvalidQuantityException
import pytest 

def test_basic_item():
    item = Item()
    assert item.type == Item_Type.Weapon 
    assert item.name == "None"
    assert item.weight == 0
    assert item.value == 0

def test_weapon():
    item = Item(name="my weapon", weight=10, value= 20, itype=Item_Type.Weapon)
    assert item.type == Item_Type.Weapon
    assert item.name == "my weapon"
    assert item.weight == 10
    assert item.value == 20
    assert item.id == "my weapon<Item_Type.Weapon: 0>"

def test_consumable():
    item = Item(name="my consumable", weight=13, value= 32, itype=Item_Type.Consumable)
    assert item.type == Item_Type.Consumable
    assert item.name == "my consumable"
    assert item.weight == 13
    assert item.value == 32
    assert item.id == "my consumable<Item_Type.Consumable: 2>"

def test_consumable():
    item = Item(name="my gear", weight=43, value= 65, itype=Item_Type.Gear)
    assert item.type == Item_Type.Gear
    assert item.name == "my gear"
    assert item.weight == 43
    assert item.value == 65
    assert item.id == "my gear<Item_Type.Gear: 1>"