from abc import ABC, abstractmethod

class Item(ABC):
    pass


class PricedItem(ABC):
    def __init__(self, item_id, price):
        self.item_id = item_id
        self.price = price
    
    @abstractmethod
    def calculate_total_price(self, quantity):
        pass

class RegularItem(PricedItem):
    def calculate_total_price(self, quantity):
        return self.price * quantity

class DiscountedItem(PricedItem):
    def calculate_total_price(self, quantity):
        return self.price * quantity

class ClearanceItem(DiscountedItem):
    def calculate_total_price(self, quantity):
        return self.price * quantity


