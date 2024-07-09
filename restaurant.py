from log import logger


class PriceValueError(Exception):
    def __init__(self, message='Price value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Price cannot be less or equals zero'


class DiscountValueError(Exception):
    def __init__(self, message='Discount value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Discount value must be greater than 0 and less than 100'


class Dish:
    def __init__(self, name: str, price: int | float):
        if not isinstance(price, int | float):
            logger.error("Price must be 'int' or 'float'")
            raise TypeError("Price must be 'int' or 'float'")
        if price < 0:
            logger.error("Price can't be less than zero")
            raise PriceValueError("Price cannot be less or equals zero")
        self.name = name
        self.price = price
        logger.debug("Dish instance was created")

    def __str__(self):
        return f'  {self.name}: {self.price}$'


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


class Discount:
    def __init__(self, discount_val: int | float = 0):
        if not isinstance(discount_val, int | float):
            logger.error("Discount value must be 'int' or 'float'")
            raise TypeError("Discount value must be 'int' or 'float'")
        if discount_val < 0 or discount_val > 100:
            logger.error("Discount value must be greater than 0 and less than 100")
            raise DiscountValueError()
        self.discount_val = discount_val
        logger.debug("Discount was set")

    def discount(self):
        """
        Return discount value
        :return: discount value
        """
        return self.discount_val

    def __str__(self):
        return f'Discount: {self.discount_val}'


class ClientOrder:
    def __init__(self, client_name: str, order: Order, discount: Discount):
        self.client_name = client_name
        self.order = order
        self.discount = discount
        logger.info("Client order was set")

    def get_total_price(self) -> int | float:
        """
        Calculate total price with discount
        :return: total price
        """
        return self.order.total() * (100 - self.discount.discount()) / 100

    def __str__(self):
        if not self.order.total():
            return f'{self.client_name}s order is empty.\n'
        return (f'{self.client_name}s order:\n{self.order}.\nDiscount: {self.discount.discount()}%.\n'
                f'Total price with discount: {self.get_total_price():.2f}$\n')


if __name__ == '__main__':
    pass
