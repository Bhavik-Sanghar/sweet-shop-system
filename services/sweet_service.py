class SweetService:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet):
        self.sweets.append(sweet)

    def get_all_sweets(self):
        return self.sweets
