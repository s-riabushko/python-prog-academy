from log import logger


class ProductPriceError(Exception):
    def __init__(self, message='Product price value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Price cannot be less or equals zero'


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


class Cart:

    def __init__(self):
        self.__products = {}
        logger.info("Cart instance was created")

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add product to the cart.
        :param product: Product object
        :param quantity: count of products
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError('Invalid product object')
        if not isinstance(quantity, int | float):
            logger.error("Invalid quantity type, must be 'int' or 'float'")
            raise TypeError("Invalid quantity type, must be 'int' or 'float'")
        if quantity < 0:
            logger.error("Quantity can't be less than zero")
            raise ValueError("Quantity can't be less than zero")

        self.__products[product] = self.__products.get(product, 0) + quantity
        logger.debug("Product was added to cart")

    def clear_cart(self):
        """
        Remove all products from the cart.
        :return: None
        """
        self.__products.clear()
        logger.debug("Cart was cleared")

    def total(self) -> float:
        """
        Calculate total cost of all products in a cart

        :return: float number
        """
        return sum(product.price * quantity for product, quantity in self.__products.items())

    def __str__(self):
        res = '\n'.join(map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]} UAH",
                            self.__products.items()))
        res += f"\nTotal: {self.total()} UAH"
        return res


if __name__ == "__main__":
    pass
