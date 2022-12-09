from decimal import Decimal
import pytest
from .coursework2.src.shopping_basket import Item, Basket

@pytest.fixture
def item(self):
    return Item("Brand", "Product", "Description", Decimal(10.0))


@pytest.fixture
def basket(self):
    return Basket()
