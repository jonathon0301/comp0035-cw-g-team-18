from decimal import Decimal
import pytest
from coursework2.src.shopping_basket import Item, Basket


@pytest.fixture
def item_1():
    item_1 = Item("Brand 1", "Product 1", "Description 1", Decimal(10.0))
    yield item_1


@pytest.fixture
def item_2():
    item_2 = Item("Brand 2", "Product 2", "Description 2", Decimal(20.0))
    yield item_2


@pytest.fixture
def basket():
    basket = Basket()
    yield basket
