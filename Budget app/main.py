"""
This module contains code for managing a personal budget.
"""
from budget import Category

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(45.67)
entertainment.withdraw(100)
business.withdraw(35.14)

print(food.get_balance())
print(entertainment.get_balance())
print(business.get_balance())

food.transfer(100, entertainment)

print(food.get_balance())
print(entertainment.get_balance())

print(food)
print(entertainment)
