# Testing

***This markdown file is used to illustrate our process of testing [shopping_basket.py](src/shopping_basket.py) file in 
the src directory by using pytest. It will also describe a range of testing techniques used including pytest fixtures, 
use of [conftest.py](test/conftest.py), coverage report, and continuous integration.***

## 1. Unit Test by Pytest

With test directory and test file already been created, we first install the pytest python library to the virtual 
environment by running ```pip install pytest``` in the terminal. After looking at the python file to be tested, we found
that there are two classes in the document, Item and Basket. The Item class contains 2 functions while the Basket class 
has 9 functions. Names and brief descriptions of each function are shown in the table below:

| Class Name | Function       | Brief Description                                                                           |
|------------|----------------|---------------------------------------------------------------------------------------------|
| **Item**   | \_\_init__     | Constructor Function to create an item with brand_name, product_name, description and price |
|            | \_\_repr__     | String Representation of an item                                                            |
| **Basket** | \_\_init__     | Constructor Function to create an empty basket that has checkout status of False            |
|            | \_\_repr__     | String Representation of a basket, gives a list of items and their quantity in the basket   |
|            | add_item       | Add an item to the basket                                                                   |
|            | remove_item    | Remove or reduce quantity of an item in the basket                                          |
|            | update_item    | Update quantity of an item in the basket                                                    |
|            | view           | Prints the contents of the basket, including quantity, price and total cost                 |
|            | get_total_cost | Calculates the total cost of the basket                                                     |
|            | reset          | Make the basket empty                                                                       |
|            | is_empty       | Check if the basket is empty or not                                                         |

### 1.1 Create fixtures in conftest.py
'conftest.py' is used to define shared fixtures and test functions that can be used across multiple test files in a 
Pytest test suite. Based on shopping_basket.py file to be tested, we have created three pytest fixtures in the conftest 
file: two different items and a basket as shown in the code below:
```
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
```
These fixtures created can be used commonly in scenarios that we intended to test, which saved time of setting items 
everytime for individual unit test.

Meanwhile, by importing necessary packages to be used in the test file within the conftest document, we do not need to 
import them again in the [test_shopping_basket](test/test_shopping_basket.py).
<details><summary>Click to see codes of importing necessary packages</summary>
<p>

```ruby
from decimal import Decimal
import pytest
from coursework2.src.shopping_basket import Item, Basket
```
</p>
</details>

### 1.2 Tests
With the preset configurations, we have tested all 11 functions in 2 classes corresponding to the shopping_basket
document in the [test_shopping_basket.py](test/test_shopping_basket.py) file. Each test is determined and described with
GIVEN-WHEN-THEN approach.
#### Class TestItem
##### Test Function 1: test_init
The first test function test_init aims to investigate whether the constructor function can return information of an item 
in the desired format. It can be described with the following GIVEN-WHEN-THEN Approach by testing with item_1 pre-defined 
in conftest.py:

"""

GIVEN an item_1 created as fixture
WHEN the item_1 passes the constructor function __init__
THEN it will return brand_name as "Brand 1", product_name as "Product 1", description as "Description 1" and
price as 10.0 in decimal

"""

Code for this test function is shown below:
```ruby
def test_init(self, item_1):
    
    assert item_1.brand_name == "Brand 1"
    assert item_1.product_name == "Product 1"
    assert item_1.description == "Description 1"
    assert item_1.price == 10.0
```
##### Test Function 2: test_repr
This test function is to test whether the _\_repr__ function can return the string representation of an item object in 
desired format. By testing with item_1 pre-defined in conftest.py, the test function can be described with GIVEN-WHEN-THEN 
Approach below:

"""

GIVEN an item_1 created as fixture
WHEN the item_1 passes the string representation function __repr__
THEN it will return a string as "Brand, Product, Description, 10"

"""

Code for this test is shown below:
```ruby
def test_repr(self, item_1):

    assert repr(item_1) == "Brand 1, Product 1, Description 1, 10"
```

#### Class TestBasket
##### Test Function 3: test_init_basket
Coming to methods in class Basket. As the same as what we did in the previous Item class, we have tested the constructor 
function. It can be described with the following GIVEN-WHEN-THEN Approach by testing with item_1 pre-defined 
in conftest.py:

"""

GIVEN an empty basket created as fixture
WHEN it passes the constructor function __init__
THEN it will return an empty set of items and checkout status of False

"""

Code for this test functions is shown below:
```ruby
def test_init_basket(self, basket):

    assert basket.items == {}
    assert basket.checkout is False
```

##### Test Function 4: test_repr_basket
The fourth test function is similar to the test function for string representation function in the Item class, which 
aims to test whether the _\_repr__ function in Basket class returns the desired format of strings. The GIVEN-WHEN-THEN 
Approach of this test function can be written as:

"""

GIVEN an empty basket and an item_1 created as fixture is added into the basket
WHEN they pass the string representation function __repr__
THEN it will return the String representation of checkout status and the list of items
and their quantity in the basket, which should be False\n<Brand, Product, Description, 10, 1>'

"""

Code for this test function:

```ruby
def test_repr_basket(self, basket, item_1):

    basket.add_item(item_1)
    assert repr(basket) == "False\n<Brand 1, Product 1, Description 1, 10, 1>"
```

##### Test Function 5: test_add_item

This test function is to investigate whether the add_item method in Basket class works properly. We have considered 5 
scenarios for this test:

1. When the basket is empty, add one item;
2. When the basket already has 1 item, add one more of the same item;
3. When the basket has 2 of the item, add 3 more of the same item;
4. When the basket has 5 of the item, add a different type of item to the basket;
5. When the basket had 5 of the item, add a negative number of item (which is not realistic), expect to raise error.

To describe the above scenarios in GIVEN-WHEN_THEN Approach:

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

Code for this test function:

```ruby
def test_add_item(self, basket, item_1, item_2):

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

```

##### Test Function 6: test_remove_item
The test function is to test the remove_item method in the Basket class, which intends to delete or reduce quantity of a 
type of item in the basket. In order to test it, we have 


