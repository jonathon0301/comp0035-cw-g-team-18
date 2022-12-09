from decimal import Decimal
import pytest
import shopping_basket
from shopping_basket import Item, Basket

@pytest.fixture
def item(self):
    return Item("Brand", "Product", "Description", Decimal(10.0))


@pytest.fixture
def basket(self):
    return Basket()
