from InventorySystem.src.Items_Types import Item_Type

class Item:
    def __init__(self, name="None", weight=0, value=0, itype=Item_Type.Weapon):
        self.id = repr(itype)
        self.Type = itype
        self.Name = name
        self.Weight = weight
        self.Value = value

    
        
