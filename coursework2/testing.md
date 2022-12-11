# Testing

***This markdown file is used to illustrate our process of testing [shopping_basket.py](src/shopping_basket.py) file in 
the src directory by using pytest. It will also describe a range of testing techniques used including pytest fixtures, 
use of [conftest.py](test/conftest.py), coverage report, and continuous integration.***

## Unit Test
We first installed the Pytest library to do unit tests based on the provided shopping_basket code. By doing the unit test, we can test our "dashboard panel" in the design section. These tests are defined and described with a "GIVEN - WHEN - THAT" method. Since each testing requires a basket for doing the unit testing. We used fixtures to provide common functions for these tests so as to make our code efficient. 

### Test 1

"""  
Given a shopping basket is empty\
When an item is added to the basket\
Then the shopping basket has 1 item

Given the basket is not cleaned and has 1 item from previous shopping\
When an item is added to the basket\
Then the shopping basket has total 2 items

Given the basket is not cleaned and has 2 item from previous shopping\
When 3 items is added to the basket\
Then the shopping basket has total 5 items

"""

### Test 2

"""\
Given a shopping basket is empty\
When an item is added to the basket and is removed from the basket\
Then the shopping basket is empty

Given a shopping basket is empty\
When 3 items are added to the basket and are removed from the basket\
Then the shopping basket is empty

Given a sh0pping basket is empty\
When 3 items are added to the basket and 2 items removed from the basket\
Then the shopping basket has left 1 item
"""

### Test 3

"""\
Given a shopping basekt has 1 item\
When 2 more items are added to the basket\
Then the shopping basket has 3 items

Given a basket is not cleaned and has 3 items from previous shopping\
When two items are now removed from the basket\
Then the shopping basket has only 1 item left

"""

### Test 4

"""\
Given 2 items are added to the shopping basket\
When these 2 items passed to "test_view" function\
Then the shopping basket has these 2 items' brand name, product type, and product descriptions and unit price of 10\
"""

### Test 5

"""\
Given a shopping basket has 2 items\
When these 2 items are passed to the "test_get_total_cost" fucntion\
Then the total cost of these two items is: 20.0\
"""


### Test 6

"""\
Given 2 items are already in a shopping basket\
When these 2 items are passed to the "test_reset" funciton\
Then the basket is reset to 0 item

"""


### Test 7

""" 
Given a basket is empty\
When an item is added to the basket\
Then the basket should not be empty

"""


## Test Results




