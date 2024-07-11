from restaurant.log import logger
from restaurant.dish import Dish


class Order:
    def __init__(self):
        self.__dishes = {}
        logger.debug("Order instance was created")

    def add_dish(self, dish: Dish, quantity: int | float = 1):
        """
        Add dish to the order.
        :param dish: Dish object
        :param quantity: quantity of dish
        :return: None
        """
        if not isinstance(dish, Dish):
            raise TypeError('Invalid dish object')
        if not isinstance(quantity, int):
            logger.error("Quantity must be integer")
            raise TypeError('Quantity must be integer')
        if quantity < 1:
            logger.error("Quantity must grater then zero")
            raise ValueError('Quantity must grater then zero')

        self.__dishes[dish] = self.__dishes.get(dish, 0) + quantity
        logger.debug("Dish added to order")

    def __iadd__(self, other: Dish):
        """
        Add dish to the order
        :param other: Dish object
        :return: changed self
        """
        if not isinstance(other, Dish):
            return NotImplemented
        self.__dishes[other] = self.__dishes.get(other, 0) + 1
        logger.debug("Dish added to order")
        return self

    def remove_dish(self, dish: Dish):
        """
        Remove dish from the order.
        :param dish: Dish object
        :return: None
        """
        if not isinstance(dish, Dish):
            raise TypeError('Invalid dish object')

        if dish not in self.__dishes:
            logger.warning("Dish not in the category")
        else:
            self.__dishes.pop(dish)
            logger.debug("Dish removed from order")

    def total(self) -> int | float:
        """
        Calculate total price by order
        :return: total price
        """
        return sum(dish.price * quantity for dish, quantity in self.__dishes.items())

    def __str__(self):
        if not self.__dishes:
            return 'There are no dishes in the order'
        res = '\n'.join(
            map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]}$", self.__dishes.items()))
        res += f"\nTotal price: {self.total()}$"
        return res
