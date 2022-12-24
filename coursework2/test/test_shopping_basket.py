from decimal import Decimal
import pytest
from coursework2.src.shopping_basket import Item, Basket


class TestItem:
    @pytest.fixture
    def item(self):
        return Item("Brand", "Product", "Description", Decimal(10.0))

    def test_init(self, item):
        """

        GIVEN an item created as fixture
        WHEN the item passes the constructor function __init__
        THEN it will return brand_name as "Brand", product_name as "Product", description as "Description" and price as
        10.0 in decimal

        """
        assert item.brand_name == "Brand"
        assert item.product_name == "Product"
        assert item.description == "Description"
        assert item.price == Decimal(10.0)

    def test_repr(self, item):
        """

        GIVEN an item created as fixture
        WHEN the item passes the string representation function __repr__
        THEN it will return a string as "Brand, Product, Description, 10"

        """
        assert repr(item) == "Brand, Product, Description, 10"


class TestBasket:
    @pytest.fixture
    def basket(self):
        return Basket()

    @pytest.fixture
    def item(self):
        return Item("Brand", "Product", "Description", Decimal(10.0))

    def test_init(self, basket):
        """

        GIVEN an empty basket created as fixture
        WHEN it passes the constructor function __init__
        THEN it will return an empty set of items and checkout status of False

        """
        assert basket.items == {}
        assert basket.checkout is False

    def test_repr(self, basket, item):
        """

        GIVEN an empty basket and an item created as fixture
        WHEN it passes the string representation function __repr__
        THEN it will return the String representation of a basket object with iteration of the list of items
        and their quantity in the basket, which should be False\n<Brand, Product, Description, 10, 1>'

        """
        basket.add_item(item)
        assert repr(basket) == "False\n<Brand, Product, Description, 10, 1>"

    def test_add_item(self, basket, item):
        """

        Given a shopping basket is empty as created in fixture
        When an item created in fixture is added to the basket with add_item method
        Then it will return information of the item and quantity of 1

        Given the basket already has 1 item created in fixture from previous shopping
        When another of the same item is added to the basket with add_item method
        Then it will return information of the item and quantity of 2

        Given the basket contains 2 items created in fixture
        When 3 more same items is added to the basket with add_item method
        Then it will return information of the item and quantity of 2

        """
        basket.add_item(item)
        assert basket.items == {item: 1}
        basket.add_item(item)
        assert basket.items == {item: 2}
        basket.add_item(item, 3)
        assert basket.items == {item: 5}

    def test_remove_item(self, basket, item):
        """

        Given a shopping basket is empty as created in fixture
        When an item created in fixture is added to the basket and then removed from the basket
        Then it will return items as an empty set

        Given a shopping basket is empty as created in fixture
        When 3 items created in fixture are added to the basket and pass the remove_item method without
        specifying quantity of removal
        Then it will return items as an empty set

        Given a shopping basket is empty as created in fixture
        When 3 items created in fixture are added to the basket and pass the remove_item method while
        specifying quantity of 2
        Then it will return the item information and quantity as 1

        """
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
        """

        Given an item created in fixture is added into a basket with add_item method
        When 2 more items are added to the basket with update_item method
        Then it will return the item information and quantity as 3

        Given a basket is not cleaned and has 3 items
        When two items are now removed from the basket with update_item method
        Then it will return the item information and quantity as 1

        """
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
        assert basket.is_empty() is True
        basket.add_item(item)
        assert basket.is_empty() is False
