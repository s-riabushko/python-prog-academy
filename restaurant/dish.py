from restaurant.log import logger
from restaurant.restaurant_exception import PriceValueError


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
