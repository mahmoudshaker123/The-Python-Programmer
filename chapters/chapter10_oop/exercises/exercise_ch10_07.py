## Exercise 10_07 - Banking System [Part 1/3]
# In the next three exercises, you will implement a simple banking system.
# Let's start first by defining our core classes (Card, Account, and Customer).

# Create two dataclasses called `Card`, `Account`, and a class called `Customer`.
# The `Card` class should have the following attributes:
# 1. card_number
# 2. card_holder
# 3. expiration_date
# 4. pin


# The `Account` class should have the following attributes:
# 1. account_number
# 2. account_holder
# 3. balance
# 4. cards (a list of `Card` instances)

from dataclasses import dataclass


@dataclass
class Card:
    # Your code should go here.
    ...


@dataclass
class Account:
    # Your code should go here.
    ...
