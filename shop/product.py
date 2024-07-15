from shop.log import logger
from shop.cart_exception import ProductPriceError


class Product:
    def __init__(self, name: str, price: int | float):
        if not isinstance(price, int | float):
            logger.error("Price must be 'int' or 'float'")
            raise TypeError("Price must be 'int' or 'float'")
        if price <= 0:
            logger.error("Price can't be less than zero")
            raise ProductPriceError("Price can't be less than zero")
        self.name = name
        self.price = price
        logger.debug("Product instance was created")

    def __str__(self):
        return f"{self.name}: {self.price} UAH"
