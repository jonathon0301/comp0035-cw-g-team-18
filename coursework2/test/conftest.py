import sys
from decimal import Decimal

import pytest

sys.path.append("../")
from src import shopping_basket


@pytest.fixture
def item(self):
    return Item("Brand", "Product", "Description", Decimal(10.0))


@pytest.fixture
def basket(self):
    return Basket()
