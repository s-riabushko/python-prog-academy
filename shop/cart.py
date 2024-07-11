from shop.product import Product
from shop.log import logger


class Cart:

    def __init__(self):
        self.__products = {}
        logger.info("Cart instance was created")

    def add_product(self, item: Product, quantity: int | float = 1):
        """
        Add product to the shop.
        :param item: Product object
        :param quantity: count of products
        :return: None
        """
        if not isinstance(item, Product):
            raise TypeError('Invalid product object')
        if not isinstance(quantity, int | float):
            logger.error("Invalid quantity type, must be 'int' or 'float'")
            raise TypeError("Invalid quantity type, must be 'int' or 'float'")
        if quantity < 0:
            logger.error("Quantity can't be less than zero")
            raise ValueError("Quantity can't be less than zero")

        self.__products[item] = self.__products.get(item, 0) + quantity
        logger.debug("Product was added to shop")

    def clear_cart(self):
        """
        Remove all products from the shop.
        :return: None
        """
        self.__products.clear()
        logger.debug("Cart was cleared")

    def total(self) -> float:
        """
        Calculate total cost of all products in a shop

        :return: float number
        """
        return sum(item.price * quantity for item, quantity in self.__products.items())

    def __iadd__(self, other):
        """
        Mixing two carts
        :param other: another Cart object
        :return: changed self
        """
        if not isinstance(other, Cart):
            return NotImplemented
        for prod_key, prod_val in other.__products.items():
            self.__products[prod_key] = self.__products.get(prod_key, 0) + prod_val
        return self

    def __str__(self):
        res = '\n'.join(map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]} UAH",
                            self.__products.items()))
        res += f"\nTotal: {self.total()} UAH"
        return res
