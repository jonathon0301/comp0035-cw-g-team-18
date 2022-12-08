import sys
from decimal import Decimal

import pytest

sys.path.append("..")
from src.shopping_basket import Item, Basket


class TestItem:
    @pytest.fixture
    def item(self):
        return Item("Brand", "Product", "Description", Decimal(10.0))

    def test_init(self, item):
        assert item.brand_name == "Brand"
        assert item.product_name == "Product"
        assert item.description == "Description"
        assert item.price == Decimal(10.0)

    def test_repr(self, item):
        assert repr(item) == "Brand, Product, Description, 10"


class TestBasket:
    @pytest.fixture
    def basket(self):
        return Basket()

    @pytest.fixture
    def item(self):
        return Item("Brand", "Product", "Description", Decimal(10.0))

    def test_init(self, basket):
        assert basket.items == {}
        assert basket.checkout == False

    def test_repr(self, basket, item):
        basket.add_item(item)
        assert repr(basket) == "False\n<Brand, Product, Description, 10, 1>"

    def test_add_item(self, basket, item):
        basket.add_item(item)
        assert basket.items == {item: 1}
        basket.add_item(item)
        assert basket.items == {item: 2}
        basket.add_item(item, 3)
        assert basket.items == {item: 5}

    def test_remove_item(self, basket, item):
        basket.add_item(item)
        basket.remove_item(item)
        assert basket.items == {}
        basket.add_item(item, 3)
        basket.remove_item(item)
        assert basket.items == {}
        basket.add_item(item, 3)
        basket.remove_item(item, 2)
        assert basket.items == {item: 1}

    def test_update_item(self, basket, item):
        basket.add_item(item)
        basket.update_item(item, 2)
        assert basket.items == {item: 3}
        basket.update_item(item, -2)
        assert basket.items == {item: 1}

    def test_view(self, basket, item, capsys):
        basket.add_item(item, 2)
        basket.view()
        captured = capsys.readouterr()
        assert captured.out == "Brand, Product, Description, 10, 2\n"

    def test_get_total_cost(self, basket, item):
        basket.add_item(item, 2)
        assert basket.get_total_cost() == Decimal(20.0)

    def test_reset(self, basket, item):
        basket.add_item(item, 2)
        basket.reset()
        assert basket.items == {}

    def test_is_empty(self, basket, item):
        assert basket.is_empty() == True
        basket.add_item(item)
