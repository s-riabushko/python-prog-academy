from restaurant.log import logger
from restaurant.dish import Dish


class Iterator:
    """
    Iterator for products
    """
    def __init__(self, dishes):
        self.dishes = dishes
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dishes):
            product = list(self.dishes.items())[self.index]
            self.index += 1
            return product
        raise StopIteration


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

    def __getitem__(self, dish):
        return list(self.__dishes.items())[dish]

    def __len__(self):
        return list(self.__dishes)

    def __iter__(self):
        return Iterator(self.__dishes)

    def __str__(self):
        if not self.__dishes:
            return 'There are no dishes in the order'
        res = '\n'.join(
            map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]}$", self.__dishes.items()))
        res += f"\nTotal price: {self.total()}$"
        return res


if __name__ == '__main__':
    onion_soup = Dish('French onion soup', 15)
    salad = Dish('Chicken Salad', 10)
    omelette = Dish('Cheese omelette', 20)
    sandwich = Dish('Chicken sandwich', 20)
    order1 = Order()
    order1.add_dish(omelette, 2)
    order1.add_dish(onion_soup, 3)
    order1.add_dish(salad, 1)
    order1.add_dish(sandwich, 1)

    iter_order = iter(order1)
    print(' x '.join(map(str, next(iter_order))))
    print(' x '.join(map(str, next(iter_order))))

    for dish, quantity in order1:
        print(f'{dish} X {quantity}')

    order1_rev = order1[::-1]
    print(type(order1_rev))
    print('\n'.join(map(lambda item: f'{item[0].name}: {item[1]}', order1_rev)))
