# Exercise 69 - TaxCalculator Class
# Define a `TaxCalculator` class that calculates the tax for a given income.
# The class should have a method `calculate_tax` that takes an income as a parameter and returns the tax amount.
# The tax should be calculated based on the following rules:
# - 0% tax for income less than or equal to 10,000
# - 10% tax for income greater than 10,000 and less than or equal to 50,000
# - 20% tax for income greater than 50,000 and less than or equal to 100,000
# - 30% tax for income greater than 100,000

# Example:
# tax_calculator = TaxCalculator()
# tax_calculator.calculate_tax(5000) => 0
# tax_calculator.calculate_tax(15000) => 500
# tax_calculator.calculate_tax(75000) => 10000


class TaxCalculator:
    def __init__(self):
        self.income = 0

    def calculate_tax(self, income: int) -> float:
        # Your code should go here.

        ...
