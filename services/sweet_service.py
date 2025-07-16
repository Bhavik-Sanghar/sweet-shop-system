class SweetService:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
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