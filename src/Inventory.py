from InventorySystem.src.InvalidQuantityException import InvalidQuantityException

class Inventory:
    def __init__(self):
        self.max_size = 25
        self.max_weight = 100
        self.current_cash = 0   
        self.items_list = []

    def pickup(self, item=None):        

        if self._itemlist_freespace() :
            if self._items_freeweight():
                self.items_list.append(item)
                return True
            else: 
                return InvalidQuantityException("Weigth exceeded")
        else: 
            return InvalidQuantityException("Space exceeded")

    def get_cash(cash):
        self.current_cash = self.current_cash + cash

    def drop(self, item):
        if item in self.items_list:
            self.items_list.remove(item)
            return True
        else:
            return False

    def current_weight(self):
        result = 0
        for item in self.items_list:
            result = result + item.Weight
        return result

    def remaining_weight(self):
        return self.max_weight - self.current_weight()

    def weight_by_type(self, itype):
        result = sum([item.Weight for item in self.items_list if item.Type == itype])
        return result

    def sell(self, item):
        if self.drop(item):
            self.current_cash = self.current_cash + item.Value
            return True
        else:
            return False

    def buy(self, item):
        if self.current_cash >= item.Value:
            self.pickup(item)      
            self.current_cash = self.current_cash - item.Value   
            return True   
        else:
            return InvalidQuantityException("Not enough money") 
        
            
        

    def _itemlist_freespace(self):
        return len(self.items_list) < self.max_size

    def _items_freeweight(self):
        result = 0
        for item in self.items_list:
            result = result + item.Weight
        return result <= self.max_weight
