## Unit Test
###We first installed the Pytest library to do unit tests based on the provided shopping_basket code. By doing the unit test, we can test our "dashboard panel" in the design section. These tests are defined and described with a "GIVEN - WHEN - THAT" method. Since each testing requires a basket for doing the unit testing. We used fixtures to provide common functions for these tests so as to make our code efficient. 

###Test 1\
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

###Test 2

