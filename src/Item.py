from InventorySystem.src.Items_Types import Item_Type

class Item:
    def __init__(self, name="None", weight=0, value=0, itype=Item_Type.Weapon):
        """
        I'm going to assume that somebody else in charge 
        of items will take care of not repeated names...        
        """
        self.id  = name + str(repr(itype))
        self.type = itype
        self.name = name
        self.weight = weight
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.id == (self.name + str(repr(other.type)))
