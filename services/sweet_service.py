from typing import List, Optional
from models.sweet import Sweet


class SweetService:
    def __init__(self) -> None:
        self.sweets: List[Sweet] = []

    def _find_sweet_by_id(self, sweet_id: int) -> Optional[Sweet]:
        """Helper method to find sweet by ID"""
        for sweet in self.sweets:
            if sweet.id == sweet_id:
                return sweet
        return None

    def add_sweet(self, sweet: Sweet) -> None:
        """Add a new sweet to the shop"""
        if any(s.id == sweet.id for s in self.sweets):
            raise ValueError(f"Sweet with ID {sweet.id} already exists")
        self.sweets.append(sweet)

    def get_all_sweets(self) -> List[Sweet]:
        """Get all sweets in the shop"""
        return self.sweets.copy()  # Return a copy to prevent external modification
    
    def delete_sweet(self, sweet_id: int) -> None:
        """Delete a sweet by ID"""
        sweet = self._find_sweet_by_id(sweet_id)
        if not sweet:
            raise ValueError(f"Sweet with ID {sweet_id} not found")
        self.sweets.remove(sweet)

    def search_by_name(self, keyword: str) -> List[Sweet]:
        """Search sweets by name (case-insensitive, partial match)"""
        if not keyword or not keyword.strip():
            return []
        keyword = keyword.strip().lower()
        return [sweet for sweet in self.sweets if keyword in sweet.name.lower()]

    def search_by_category(self, category: str) -> List[Sweet]:
        """Search sweets by category (case-insensitive, exact match)"""
        if not category or not category.strip():
            return []
        category = category.strip().lower()
        return [sweet for sweet in self.sweets if sweet.category.lower() == category]
    
    def search_by_price_range(self, min_price: float, max_price: float) -> List[Sweet]:
        """Search sweets within a price range"""
        if min_price < 0 or max_price < 0:
            raise ValueError("Price range values must be non-negative")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price")
        return [sweet for sweet in self.sweets if min_price <= sweet.price <= max_price]
    
    def purchase_sweet(self, sweet_id: int, quantity: int) -> None:
        """Purchase sweets, reducing stock quantity"""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        
        sweet = self._find_sweet_by_id(sweet_id)
        if not sweet:
            raise ValueError(f"Sweet with ID {sweet_id} not found")
        
        if sweet.quantity < quantity:
            raise ValueError(f"Insufficient stock. Available: {sweet.quantity}, Requested: {quantity}")
        
        sweet.quantity -= quantity

    def restock_sweet(self, sweet_id: int, quantity: int) -> None:
        """Restock sweets, increasing stock quantity"""
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        
        sweet = self._find_sweet_by_id(sweet_id)
        if not sweet:
            raise ValueError(f"Sweet with ID {sweet_id} not found")
        
        sweet.quantity += quantity

    def sort_by_name(self, descending: bool = False) -> List[Sweet]:
        """Sort sweets by name"""
        return sorted(self.sweets, key=lambda sweet: sweet.name.lower(), reverse=descending)
    
    def sort_by_price(self, descending: bool = False) -> List[Sweet]:
        """Sort sweets by price"""
        return sorted(self.sweets, key=lambda sweet: sweet.price, reverse=descending)

    def sort_by_quantity(self, descending: bool = False) -> List[Sweet]:
        """Sort sweets by quantity"""
        return sorted(self.sweets, key=lambda sweet: sweet.quantity, reverse=descending)
    
    def sort_by_category(self, descending: bool = False) -> List[Sweet]:
        """Sort sweets by category"""
        return sorted(self.sweets, key=lambda sweet: sweet.category.lower(), reverse=descending)

    def get_low_stock_sweets(self, threshold: int = 5) -> List[Sweet]:
        """Get sweets with low stock"""
        return [sweet for sweet in self.sweets if sweet.quantity <= threshold]

    def get_total_value(self) -> float:
        """Calculate total value of inventory"""
        return sum(sweet.price * sweet.quantity for sweet in self.sweets)