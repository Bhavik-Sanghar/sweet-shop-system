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
