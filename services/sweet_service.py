class SweetService:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)

    def get_all_sweets(self):
        return self.sweets
    
    def delete_sweet(self, sweet_id):
        self.sweets = [s for s in self.sweets if s.id != sweet_id]

    def search_by_name(self, keyword):
        return [sweet for sweet in self.sweets if keyword.lower() in sweet.name.lower()]

    def search_by_category(self, category):
        return [sweet for sweet in self.sweets if sweet.category.strip().lower() == category.strip().lower()]