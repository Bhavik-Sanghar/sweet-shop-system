class Sweet:
    def __init__(self, sweet_id: int, name: str, category: str, price: float, quantity: int):
        # Validate inputs
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not category or not category.strip():
            raise ValueError("Category cannot be empty")
        if not isinstance(sweet_id, int) or sweet_id <= 0:
            raise ValueError("Sweet ID must be a positive integer")
        
        self.id = sweet_id
        self.name = name.strip()
        self.category = category.strip()
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Sweet(id={self.id}, name='{self.name}', category='{self.category}', "
                f"price={self.price}, quantity={self.quantity})")

    def __eq__(self, other):
        if not isinstance(other, Sweet):
            return False
        return self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }