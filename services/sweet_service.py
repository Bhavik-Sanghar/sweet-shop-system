class SweetService:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        if sweet.price <= 0:
            raise ValueError("Price must be positive")
        if sweet.quantity <= 0:
            raise ValueError("Quantity must be positive")
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError(f"Sweet with ID {sweet.id} already exists")
        self.sweets.append(sweet)



    def get_all_sweets(self):
        return self.sweets
    
    def delete_sweet(self, sweet_id):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                self.sweets.remove(sweet)
                return
        raise ValueError(f"Sweet with ID {sweet_id} not found")


    def search_by_name(self, keyword):
        return [sweet for sweet in self.sweets if keyword.lower() in sweet.name.lower()]

    def search_by_category(self, category):
        return [sweet for sweet in self.sweets if sweet.category.strip().lower() == category.strip().lower()]
    
    def search_by_price_range(self, min_price, max_price):
        return [sweet for sweet in self.sweets if min_price <= sweet.price <= max_price]
    
    def purchase_sweet(self, sweet_id, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                if sweet.quantity < quantity:
                    raise ValueError("Insufficient stock")
                sweet.quantity -= quantity
                return
        raise ValueError(f"Sweet with ID {sweet_id} not found")


    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                if quantity <= 0:
                    raise ValueError("Restock quantity must be positive")
                sweet.quantity += quantity
                return
        raise ValueError(f"Sweet with ID {sweet_id} not found")

    def sort_by_name(self):
        return sorted(self.sweets, key=lambda sweet: sweet.name.lower())
    
    def sort_by_price(self, descending=False):
        return sorted(self.sweets, key=lambda sweet: sweet.price, reverse=descending)

    def sort_by_quantity(self, descending=False):
        return sorted(self.sweets, key=lambda sweet: sweet.quantity, reverse=descending) 