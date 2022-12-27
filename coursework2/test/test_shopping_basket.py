class TestItem:

    def test_init(self, item_1):
        """

        GIVEN an item_1 created as fixture
        WHEN the item_1 passes the constructor function __init__
        THEN it will return brand_name as "Brand 1", product_name as "Product 1", description as "Description 1" and
        price as 10.0 in decimal

        """
        assert item_1.brand_name == "Brand 1"
        assert item_1.product_name == "Product 1"
        assert item_1.description == "Description 1"
        assert item_1.price == 10.0

    def test_repr(self, item_1):
        """

        GIVEN an item_1 created as fixture
        WHEN the item_1 passes the string representation function __repr__
        THEN it will return a string as "Brand, Product, Description, 10"

        """
        assert repr(item_1) == "Brand 1, Product 1, Description 1, 10"


class TestBasket:

    def test_init_basket(self, basket):
        """

        GIVEN an empty basket created as fixture
        WHEN it passes the constructor function __init__
        THEN it will return an empty set of items and checkout status of False

        """
        assert basket.items == {}
        assert basket.checkout is False

    def test_repr_basket(self, basket, item_1):
        """

        GIVEN an empty basket and an item_1 created as fixture is added into the basket
        WHEN they pass the string representation function __repr__
        THEN it will return the String representation of checkout status and the list of items
        and their quantity in the basket, which should be False\n<Brand, Product, Description, 10, 1>'

        """
        basket.add_item(item_1)
        assert repr(basket) == "False\n<Brand 1, Product 1, Description 1, 10, 1>"

    def test_add_item(self, basket, item_1, item_2):
        """

        GIVEN a shopping basket is empty as created in fixture
        WHEN an item_1 created in fixture is added to the basket with add_item method
        THEN it will return information of the item_1 and quantity of 1

        GIVEN the basket already has 1 item created in fixture from previous shopping
        WHEN another of the same item is added to the basket with add_item method
        THEN it will return information of the item and quantity of 2

        GIVEN the basket contains 2 items created in fixture
        WHEN 3 more same items is added to the basket with add_item method
        THEN it will return information of the item and quantity of 5

        GIVEN the basket contains 5 items created in fixture
        WHEN another type of item named item_2 is added to the basket with add_item method
        THEN it will return information of the original item and quantity 5 with information of item_1 and quantity 1

        GIVEN the basket contains 5 items created in fixture
        WHEN a non-positive number of items is added with add_item method
        THEN it will raise ValueError

        """
        basket.add_item(item_1)
        assert basket.items == {item_1: 1}
        basket.add_item(item_1)
        assert basket.items == {item_1: 2}
        basket.add_item(item_1, 3)
        assert basket.items == {item_1: 5}
        basket.add_item(item_2)
        assert basket.items == {item_1: 5,
                                item_2: 1}
        basket.remove_item(item_2)
        basket.add_item(item_1, -1)
        assert ValueError
        basket.add_item(item_1, 0)
        assert ValueError

    def test_remove_item(self, basket, item_1):
        """
        GIVEN a shopping basket is empty as created in fixture
        WHEN the empty basket passes the remove_item method asked to delete one item_1
        THEN it will return items as an empty set

        GIVEN a shopping basket is empty as created in fixture
        WHEN an item created in fixture is added to the basket and then removed from the basket
        THEN it will return items as an empty set

        GIVEN a shopping basket is empty as created in fixture
        WHEN 3 items created in fixture are added to the basket and pass the remove_item method without
        specifying quantity of removal
        THEN it will return items as an empty set

        GIVEN a shopping basket is empty as created in fixture
        WHEN 3 items created in fixture are added to the basket and pass the remove_item method while
        specifying quantity of 2
        THEN it will return the item information and quantity as 1

        GIVEN 3 items are added into shopping basket
        WHEN the basket passes remove_item function with non-positive quantity (0 & -1)
        THEN it will return items as an empty set

        """
        basket.remove_item(item_1)
        assert basket.items == {}
        basket.add_item(item_1)
        basket.remove_item(item_1)
        assert basket.items == {}
        basket.add_item(item_1, 3)
        basket.remove_item(item_1)
        assert basket.items == {}
        basket.add_item(item_1, 3)
        basket.remove_item(item_1, 2)
        assert basket.items == {item_1: 1}
        basket.remove_item(item_1, 3)
        assert basket.items == {}
        basket.add_item(item_1, 3)
        basket.remove_item(item_1, 0)
        assert basket.items == {}
        basket.add_item(item_1, 3)
        basket.remove_item(item_1, -1)
        assert basket.items == {}

    def test_update_item(self, basket, item_1):
        """

        GIVEN an item created in fixture is added into a basket with add_item method
        WHEN the quantity of item is changed to 2 with update_item method
        THEN it will return the item information and quantity as 2

        GIVEN a basket is not cleaned and has 2 items
        WHEN a negative quantity is passed with update_item method
        THEN it will return an empty set

        """
        basket.add_item(item_1)
        basket.update_item(item_1, 2)
        assert basket.items == {item_1: 2}
        basket.update_item(item_1, -2)
        assert basket.items == {}

    def test_view(self, basket, item_1, capsys):
        """

        GIVEN 2 items created in fixture are added to the shopping basket with add_item function
        WHEN these 2 items passed to "test_view" function
        THEN it will return the contents of the basket including quantity, price and total cost.

        """
        basket.add_item(item_1, 2)
        basket.view()
        captured = capsys.readouterr()
        assert captured.out == """---------------------\n + Brand 1 Product 1 - 2 x £10.00 = £20.00
---------------------\nBasket total = £20.00\n---------------------\n"""

    def test_get_total_cost(self, basket, item_1):
        """

        GIVEN two items created in fixture are added into the basket with add_item method
        WHEN the basket passes get_total_cost method
        THEN it will return a decimal total cost for two items as 20.0

        """
        basket.add_item(item_1, 2)
        assert basket.get_total_cost() == 20.0

    def test_reset(self, basket, item_1):
        """

        GIVEN two items created in fixture are added into the basket with add_item method
        WHEN the basket passes reset method
        THEN it will return the basket as empty

        """
        basket.add_item(item_1, 2)
        basket.reset()
        assert basket.items == {}

    def test_is_empty(self, basket, item_1):
        """

        GIVEN an empty basket created in fixture
        WHEN the basket passes is_empty function
        THEN it will return True

        GIVEN an item created in fixture is added into the basket with add_item method
        WHEN the basket passes is_empty function
        THEN it will return False

        """
        assert basket.is_empty() is True
        basket.add_item(item_1)
        assert basket.is_empty() is False
