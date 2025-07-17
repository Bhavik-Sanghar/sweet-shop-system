import pytest
from services.sweet_service import SweetService
from models.sweet import Sweet


class TestSweetModel:
    """Test cases for Sweet model validation"""
    
    def test_create_valid_sweet(self):
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
        assert sweet.id == 1001
        assert sweet.name == "Kaju Katli"
        assert sweet.category == "Nut-Based"
        assert sweet.price == 50.0
        assert sweet.quantity == 20

    def test_create_sweet_with_negative_price_raises_error(self):
        with pytest.raises(ValueError, match="Price must be positive"):
            Sweet(1001, "Kaju Katli", "Nut-Based", -50.0, 10)

    def test_create_sweet_with_zero_price_raises_error(self):
        with pytest.raises(ValueError, match="Price must be positive"):
            Sweet(1001, "Kaju Katli", "Nut-Based", 0.0, 10)

    def test_create_sweet_with_negative_quantity_raises_error(self):
        with pytest.raises(ValueError, match="Quantity cannot be negative"):
            Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, -5)

    def test_create_sweet_with_empty_name_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Sweet(1001, "", "Nut-Based", 50.0, 10)

    def test_create_sweet_with_whitespace_name_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Sweet(1001, "   ", "Nut-Based", 50.0, 10)

    def test_create_sweet_with_empty_category_raises_error(self):
        with pytest.raises(ValueError, match="Category cannot be empty"):
            Sweet(1001, "Kaju Katli", "", 50.0, 10)

    def test_create_sweet_with_invalid_id_raises_error(self):
        with pytest.raises(ValueError, match="Sweet ID must be a positive integer"):
            Sweet(0, "Kaju Katli", "Nut-Based", 50.0, 10)

    def test_sweet_strips_whitespace_from_name_and_category(self):
        sweet = Sweet(1001, "  Kaju Katli  ", "  Nut-Based  ", 50.0, 10)
        assert sweet.name == "Kaju Katli"
        assert sweet.category == "Nut-Based"


class TestSweetService:
    """Test cases for SweetService functionality"""
    
    @pytest.fixture
    def service(self):
        return SweetService()

    @pytest.fixture
    def service_with_sample_data(self):
        service = SweetService()
        service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20))
        service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 30.0, 10))
        service.add_sweet(Sweet(1003, "Kaju Pista Roll", "Nut-Based", 40.0, 15))
        return service

    # Add Sweet Tests
    def test_add_sweet_successfully(self, service):
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
        service.add_sweet(sweet)
        
        all_sweets = service.get_all_sweets()
        assert len(all_sweets) == 1
        assert all_sweets[0].name == "Kaju Katli"

    def test_add_duplicate_id_raises_error(self, service):
        sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50.0, 20)
        sweet2 = Sweet(1001, "Rasgulla", "Milk-Based", 25.0, 10)

        service.add_sweet(sweet1)
        with pytest.raises(ValueError, match="Sweet with ID 1001 already exists"):
            service.add_sweet(sweet2)

    # Get All Sweets Tests
    def test_get_all_sweets_returns_copy(self, service_with_sample_data):
        all_sweets = service_with_sample_data.get_all_sweets()
        all_sweets.clear()  # Modify the returned list
        
        # Original data should remain unchanged
        assert len(service_with_sample_data.get_all_sweets()) == 3

    def test_get_all_sweets_empty_service(self, service):
        all_sweets = service.get_all_sweets()
        assert len(all_sweets) == 0

    # Delete Sweet Tests
    def test_delete_sweet_by_id(self, service_with_sample_data):
        service_with_sample_data.delete_sweet(1001)
        all_sweets = service_with_sample_data.get_all_sweets()
        
        assert len(all_sweets) == 2
        assert not any(sweet.id == 1001 for sweet in all_sweets)

    def test_delete_sweet_invalid_id_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Sweet with ID 9999 not found"):
            service_with_sample_data.delete_sweet(9999)

    # Search by Name Tests
    def test_search_sweets_by_name_partial_match(self, service_with_sample_data):
        results = service_with_sample_data.search_by_name("Kaju")
        
        assert len(results) == 2
        assert all("Kaju" in sweet.name for sweet in results)

    def test_search_sweets_by_name_case_insensitive(self, service_with_sample_data):
        results = service_with_sample_data.search_by_name("kaju")
        
        assert len(results) == 2
        assert all("Kaju" in sweet.name for sweet in results)

    def test_search_by_name_returns_empty_list_when_no_match(self, service_with_sample_data):
        results = service_with_sample_data.search_by_name("Chocolate")
        assert len(results) == 0

    def test_search_by_name_empty_keyword_returns_empty_list(self, service_with_sample_data):
        results = service_with_sample_data.search_by_name("")
        assert len(results) == 0

    # Search by Category Tests
    def test_search_sweets_by_category(self, service_with_sample_data):
        results = service_with_sample_data.search_by_category("Nut-Based")
        
        assert len(results) == 2
        assert all(sweet.category == "Nut-Based" for sweet in results)

    def test_search_sweets_by_category_case_insensitive(self, service_with_sample_data):
        results = service_with_sample_data.search_by_category("nut-based")
        
        assert len(results) == 2
        assert all(sweet.category == "Nut-Based" for sweet in results)

    def test_search_by_category_empty_returns_empty_list(self, service_with_sample_data):
        results = service_with_sample_data.search_by_category("")
        assert len(results) == 0

    # Search by Price Range Tests
    def test_search_sweets_by_price_range(self, service_with_sample_data):
        results = service_with_sample_data.search_by_price_range(30.0, 50.0)
        
        assert len(results) == 3
        assert all(30.0 <= sweet.price <= 50.0 for sweet in results)

    def test_search_by_price_range_boundary_values(self, service_with_sample_data):
        results = service_with_sample_data.search_by_price_range(30.0, 30.0)
        
        assert len(results) == 1
        assert results[0].price == 30.0

    def test_search_by_price_range_negative_values_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Price range values must be non-negative"):
            service_with_sample_data.search_by_price_range(-10.0, 50.0)

    def test_search_by_price_range_min_greater_than_max_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Minimum price cannot be greater than maximum price"):
            service_with_sample_data.search_by_price_range(50.0, 30.0)

    # Purchase Sweet Tests
    def test_purchase_sweet_reduces_quantity(self, service_with_sample_data):
        service_with_sample_data.purchase_sweet(1001, 5)
        
        sweet = service_with_sample_data._find_sweet_by_id(1001)
        assert sweet.quantity == 15

    def test_purchase_sweet_exact_stock_amount(self, service_with_sample_data):
        service_with_sample_data.purchase_sweet(1002, 10)
        
        sweet = service_with_sample_data._find_sweet_by_id(1002)
        assert sweet.quantity == 0

    def test_purchase_sweet_insufficient_stock_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Insufficient stock. Available: 10, Requested: 15"):
            service_with_sample_data.purchase_sweet(1002, 15)

    def test_purchase_sweet_invalid_id_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Sweet with ID 9999 not found"):
            service_with_sample_data.purchase_sweet(9999, 1)

    def test_purchase_sweet_zero_quantity_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Purchase quantity must be positive"):
            service_with_sample_data.purchase_sweet(1001, 0)

    def test_purchase_sweet_negative_quantity_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Purchase quantity must be positive"):
            service_with_sample_data.purchase_sweet(1001, -5)

    # Restock Sweet Tests
    def test_restock_sweet_increases_quantity(self, service_with_sample_data):
        service_with_sample_data.restock_sweet(1001, 10)
        
        sweet = service_with_sample_data._find_sweet_by_id(1001)
        assert sweet.quantity == 30

    def test_restock_sweet_invalid_id_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Sweet with ID 9999 not found"):
            service_with_sample_data.restock_sweet(9999, 10)

    def test_restock_sweet_zero_quantity_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Restock quantity must be positive"):
            service_with_sample_data.restock_sweet(1001, 0)

    def test_restock_sweet_negative_quantity_raises_error(self, service_with_sample_data):
        with pytest.raises(ValueError, match="Restock quantity must be positive"):
            service_with_sample_data.restock_sweet(1001, -5)

    # Sort Tests
    def test_sort_sweets_by_name_ascending(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_name()
        sorted_names = [sweet.name for sweet in sorted_sweets]
        
        assert sorted_names == ["Gulab Jamun", "Kaju Katli", "Kaju Pista Roll"]

    def test_sort_sweets_by_name_descending(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_name(descending=True)
        sorted_names = [sweet.name for sweet in sorted_sweets]
        
        assert sorted_names == ["Kaju Pista Roll", "Kaju Katli", "Gulab Jamun"]

    def test_sort_sweets_by_price_ascending(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_price()
        sorted_prices = [sweet.price for sweet in sorted_sweets]
        
        assert sorted_prices == [30.0, 40.0, 50.0]

    def test_sort_sweets_by_price_descending(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_price(descending=True)
        sorted_prices = [sweet.price for sweet in sorted_sweets]
        
        assert sorted_prices == [50.0, 40.0, 30.0]

    def test_sort_sweets_by_quantity_descending(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_quantity(descending=True)
        sorted_quantities = [sweet.quantity for sweet in sorted_sweets]
        
        assert sorted_quantities == [20, 15, 10]

    def test_sort_sweets_by_category(self, service_with_sample_data):
        sorted_sweets = service_with_sample_data.sort_by_category()
        sorted_categories = [sweet.category for sweet in sorted_sweets]
        
        assert sorted_categories == ["Milk-Based", "Nut-Based", "Nut-Based"]