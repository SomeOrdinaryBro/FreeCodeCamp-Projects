"""
This module provides a Category class and a create_spend_chart function.
"""
class Category:
    """
    A class for representing a category in a budget.
    
    """
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Adds a deposit to the category's ledger.
        
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Withdraws an amount from the category's ledger.
        
        """
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        """
        Returns the balance of the category.
        
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfers an amount from the category to another category.

        """
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        """
        Checks if the category has enough funds to make a withdrawal or transfer.

        """
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = "".join([f"{item['description'][:23]:23}{item['amount']:>7.2f}\n" for item in self.ledger])
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """
    Creates a chart showing the percentage of withdrawals for each category.
    """
    withdrawals = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_withdrawals = sum(withdrawals)
    withdrawals_percentages = [int(w / total_withdrawals * 10) * 10 for w in withdrawals]
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in withdrawals_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
    return chart
