"""
Module for testing the budget class.
"""
import unittest
import budget
from budget import create_spend_chart



class UnitTests(unittest.TestCase):
    """
    A class for unit testing.
    """
    maxDiff = None

    def setUp(self):
        """
        A method that will run before each test method is executed.
        """
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit(self):
        """
        A method to test the `deposit` function.
        """
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        self.assertEqual(actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')

    def test_deposit_no_description(self):
        """
        A method to test the `deposit` function with no description.
        """
        self.food.deposit(45.56)
        actual = self.food.ledger[0]
        expected = {"amount": 45.56, "description": ""}
        self.assertEqual(actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

    def test_withdraw(self):
        """
        A method to test the `withdraw` function.
        """
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
        self.assertEqual(actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

    def test_withdraw_no_description(self):
        """
        A method to test the `withdraw` function with no description.
        """
        self.food.deposit(900, "deposit")
        good_withdraw = self.food.withdraw(45.67)
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": ""}
        self.assertEqual(actual, expected, 'Expected `withdraw` method with no description to create a blank description.')
        self.assertEqual(good_withdraw, True, 'Expected `withdraw` method to return `True`.')

    def test_get_balance(self):
        """
        A method to test the `get_balance` function.
        """
        self.food.deposit(900, "deposit")
        self.assertEqual(self.food.get_balance(), 900, 'Expected balance of 900')
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.assertEqual(self.food.get_balance(), 854.33, 'Expected balance of 854.33')

    def test_transfer(self):
        """
        A method to test the `transfer` function.
        """
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        transfer_amount = 20
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount, "description": "Transfer to Entertainment"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
        self.assertEqual(good_transfer, True, 'Expected transfer method to return True.')
        self.assertEqual(food_balance_before-transfer_amount, food_balance_after, 'Expected balance in food object to decrease by the transferred amount.')
        self.assertEqual(entertainment_balance_before+transfer_amount, entertainment_balance_after, 'Expected balance in entertainment object to increase by the transferred amount.')

    def test_transfer_insufficient_funds(self):
        """
        A method to test the `transfer` function when there are insufficient funds.
        """
        self.food.deposit(50, "deposit")
        transfer_amount = 100
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        self.assertEqual(good_transfer, False, 'Expected `transfer` method with insufficient funds to return `False`.')
        self.assertEqual(self.food.get_balance(), 50, 'Expected balance in food object to remain the same.')
        self.assertEqual(self.entertainment.get_balance(), 0, 'Expected balance in entertainment object to remain the same.')

    def test_check_funds(self):
        """
        A method to test the `check_funds` function.
        """
        self.food.deposit(500, "deposit")
        self.assertEqual(self.food.check_funds(50), True, 'Expected `check_funds` method to return `True`.')
        self.assertEqual(self.food.check_funds(500), True, 'Expected `check_funds` method to return `True`.')
        self.assertEqual(self.food.check_funds(550), False, 'Expected `check_funds` method to return `False`.')

    def test_create_spend_chart(self):
        """
        A method to test the `create_spend_chart` function.
        """
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

if __name__ == "__main__":
    unittest.main()
