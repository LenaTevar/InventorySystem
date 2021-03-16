from InventorySystem.src.InvalidQuantityException import InvalidQuantityException

class Inventory:
    def __init__(self):
        self.max_size = 25
        self.max_weight = 100
        self.current_cash = 0   
        self.items_list = []

    def pickup(self, item):
        if self._itemlist_freespace() :
            if self._items_freeweight():
                self.items_list.append(item)
                return True
            else: 
                return InvalidQuantityException("Weigth exceeded")
        else: 
            return InvalidQuantityException("Space exceeded")

    
    def _itemlist_freespace(self):
        return len(self.items_list) < self.max_size

    def _items_freeweight(self):
        result = 0
        for item in self.items_list:
            result = result + item.Weight
        return result <= self.max_weight
