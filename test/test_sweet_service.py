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
