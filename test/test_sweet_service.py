import pytest
from services.sweet_service import SweetService
from models.sweet import Sweet

def test_get_all_sweets_returns_all_added_sweets():
    service = SweetService()
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
    sweet2 = Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 10)

    service.add_sweet(sweet1)
    service.add_sweet(sweet2)

    all_sweets = service.get_all_sweets()

    assert len(all_sweets) == 2
    assert all_sweets[0].name == "Kaju Katli"
    assert all_sweets[1].name == "Gulab Jamun"


def test_delete_sweet_by_id():
    service = SweetService()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
    service.add_sweet(sweet)

    service.delete_sweet(1001)
    all_sweets = service.get_all_sweets()

    assert len(all_sweets) == 0
    

def test_search_sweets_by_name_partial_match():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Roll", "Nut-Based", 50.0, 20))
    service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 10))
    service.add_sweet(Sweet(1003, "Kaju Pista Roll", "Nut-Based", 40.0, 15))

    results = service.search_by_name("Roll")

    assert len(results) == 2
    assert all("Roll" in sweet.name for sweet in results)

def test_search_sweets_by_category():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20))
    service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 10))
    service.add_sweet(Sweet(1003, "Kaju Pista Roll", "Nut-Based", 40.0, 15))
    service.add_sweet(Sweet(1004, "Rasgulla", "Milk-Based", 25.0, 5))
    
    results = service.search_by_category("Nut-Based")

    assert len(results) == 2
    assert all("Nut-Based" in sweet.category for sweet in results)
    
def test_search_sweets_by_price_range():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20))
    service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 10))
    service.add_sweet(Sweet(1003, "Peda", "Milk-Based", 20.0, 5))

    results = service.search_by_price_range(25.0, 50.0)

    assert len(results) == 2
    assert all(25.0 <= sweet.price <= 50.0 for sweet in results)
    

def test_delete_sweet_invalid_id_raises_error():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20))

    with pytest.raises(ValueError, match="Sweet with ID 9999 not found"):
        service.delete_sweet(9999)

def test_add_duplicate_id_raises_error():
    service = SweetService()
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
    sweet2 = Sweet(1001, "Rasgulla", "Milk-Based", 25.0, 10)

    service.add_sweet(sweet1)
    with pytest.raises(ValueError, match="Sweet with ID 1001 already exists"):
        service.add_sweet(sweet2)

def test_purchase_sweet_reduces_quantity():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 10))

    service.purchase_sweet(1001, 4)
    all_sweets = service.get_all_sweets()

    assert all_sweets[0].quantity == 6

def test_restock_sweet_increases_quantity():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 5))

    service.restock_sweet(1001, 10)
    all_sweets = service.get_all_sweets()

    assert all_sweets[0].quantity == 15

    
def test_sort_sweets_by_name():
    service = SweetService()
    service.add_sweet(Sweet(1003, "Peda", "Milk-Based", 20.0, 5))
    service.add_sweet(Sweet(1001, "Barfi", "Milk-Based", 40.0, 10))
    service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 15))

    sorted_sweets = service.sort_by_name()
    sorted_names = [sweet.name for sweet in sorted_sweets]

    assert sorted_names == ["Barfi", "Gulab Jamun", "Peda"]

def test_sort_sweets_by_price_ascending():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Barfi", "Milk-Based", 40.0, 10))
    service.add_sweet(Sweet(1002, "Peda", "Milk-Based", 20.0, 5))
    service.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 30.0, 15))

    sorted_sweets = service.sort_by_price()
    sorted_prices = [sweet.price for sweet in sorted_sweets]

    assert sorted_prices == [20.0, 30.0, 40.0]

def test_sort_sweets_by_price_descending():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Barfi", "Milk-Based", 40.0, 10))
    service.add_sweet(Sweet(1002, "Peda", "Milk-Based", 20.0, 5))
    service.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 30.0, 15))

    sorted_sweets = service.sort_by_price(descending=True)
    sorted_prices = [sweet.price for sweet in sorted_sweets]

    assert sorted_prices == [40.0, 30.0, 20.0]
    
def test_sort_sweets_by_quantity_descending():
    service = SweetService()
    service.add_sweet(Sweet(1001, "Peda", "Milk-Based", 20.0, 5))
    service.add_sweet(Sweet(1002, "Barfi", "Milk-Based", 30.0, 15))
    service.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 25.0, 10))

    sorted_sweets = service.sort_by_quantity(descending=True)
    sorted_quantities = [sweet.quantity for sweet in sorted_sweets]

    assert sorted_quantities == [15, 10, 5]
    
def test_add_sweet_with_negative_price_raises_error():
    service = SweetService()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", -50.0, 10)

    with pytest.raises(ValueError, match="Price must be positive"):
        service.add_sweet(sweet)

def test_add_sweet_with_zero_quantity_raises_error():
    service = SweetService()
    sweet = Sweet(1002, "Rasgulla", "Milk-Based", 25.0, 0)

    with pytest.raises(ValueError, match="Quantity must be positive"):
        service.add_sweet(sweet)

