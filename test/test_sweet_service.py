import pytest
from services.sweet_service import SweetService
from models.sweet import Sweet

def test_add_sweet_successfully():
    service = SweetService()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
    
    service.add_sweet(sweet)
    all_sweets = service.get_all_sweets()

    assert len(all_sweets) == 1
    assert all_sweets[0].name == "Kaju Katli"

def test_delete_sweet_by_id():
    service = SweetService()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
    service.add_sweet(sweet)

    service.delete_sweet(1001)
    all_sweets = service.get_all_sweets()

    assert len(all_sweets) == 0
