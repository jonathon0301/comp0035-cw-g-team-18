from decimal import Decimal
import pytest
import shopping_basket.Item
import shopping_basket.Basket


@pytest.fixture
def item(self):
    return Item("Brand", "Product", "Description", Decimal(10.0))


@pytest.fixture
def basket(self):
    return Basket()
