from restaurant.log import logger
from restaurant.restaurant_exception import DiscountValueError


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
