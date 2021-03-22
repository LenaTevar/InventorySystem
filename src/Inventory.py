from InventorySystem.src.InvalidQuantityException import InvalidQuantityException

class Inventory:
    def __init__(self):
        self.max_size = 25
        self.max_weight = 100
        self.current_cash = 0   
        self.items_list = []

    def pickup(self, item):
        if not self._itemlist_freespace():
            raise InvalidQuantityException("Inventory full")
        if not self._items_freeweight(item.weight):
            raise InvalidQuantityException("Weight full")
        else:
            self.items_list.append(item)
            return True

    def get_cash(self,cash):
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
            result = result + item.weight
        return result

    def remaining_weight(self):
        return self.max_weight - self.current_weight()

    def weight_by_type(self, itype):
        result = sum([item.weight for item in self.items_list if item.type == itype])
        return result

    def sell(self, item):
        if self.drop(item):
            self.current_cash = self.current_cash + item.value
            return True
        else:
            return False

    def buy(self, item):
        if self.current_cash >= item.value:
            self.pickup(item)      
            self.current_cash = self.current_cash - item.value   
            return True   
        else:
            raise InvalidQuantityException("Not enough money") 
        
    def get_totalnr_items(self):
        return len(self.items_list)
    
    def get_free_space(self):
        return self.max_size - len(self.items_list)
        
    def get_items_by_type(self, itype):
        return [item for item in  self.items_list if item.type == itype]

    def items_sort_value(self):
        result = sorted(self.items_list, key=lambda item: item.value)
        return result

    def items_sort_weight(self):
        result = sorted(self.items_list, key=lambda item: item.weight)
        return result

  

    ##########################################################
    #
    #   
    #
    ##########################################################
    def _itemlist_freespace(self):
        return len(self.items_list) < self.max_size

    def _items_freeweight(self, item_weight):
        result = self.remaining_weight() - item_weight
        if result > 0: 
            return True
        else:
            return False
