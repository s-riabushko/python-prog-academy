from shop.product import Product
from shop.log import logger


class Iterator:
    """
    Iterator for products
    """
    def __init__(self, products, quantities):
        self.products = products
        self.quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            quantity = self.quantities[self.index]
            self.index += 1
            return product, quantity
        raise StopIteration


class Cart:
    """
    Class Cart -- container for product
    """
    def __init__(self):
        self.__products = []
        self.__quantities = []
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
        if item in self.__products:
            product_index = self.__products.index(item)
            self.__quantities[product_index] += quantity
        else:
            self.__products.append(item)
            self.__quantities.append(quantity)
        logger.debug("Product was added to shop")

    def __iadd__(self, other):
        """
        Mixing two carts
        :param other: another Cart object
        :return: changed self
        """
        if not isinstance(other, Cart):
            return NotImplemented
        for other_product in other.__products:
            other_quantity = other.__quantities[other.__products.index(other_product)]
            if other_product in self.__products:
                product_index = self.__products.index(other_product)
                self.__quantities[product_index] += other_quantity
            else:
                self.__products.append(other_product)
                self.__quantities.append(other_quantity)
        return self

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
        return sum(item.price * quantity for item, quantity in zip(self.__products, self.__quantities))

    def __iter__(self):
        return Iterator(self.__products, self.__quantities)

    def __str__(self):
        res = '\n'.join(map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]} UAH",
                            zip(self.__products, self.__quantity)))
        res += f"\nTotal: {self.total()} UAH"
        return res


if __name__ == '__main__':
    pr_1 = Product("Bread", 10)
    pr_2 = Product("Milk", 20)
    pr_3 = Product("Butter", 30)
    pr_4 = Product("Olive oil", 25)
    cart_1 = Cart()
    cart_1.add_product(pr_1, 2)
    cart_1.add_product(pr_2, 3)
    cart_1.add_product(pr_3, 2)
    cart_2 = Cart()
    cart_2.add_product(pr_3, 3)
    cart_2.add_product(pr_4, 2)
    cart_1 += cart_2

    iter_cart = iter(cart_1)
    print(' x '.join(map(str, next(iter_cart))))
    print(' x '.join(map(str, next(iter_cart))))
    print(' x '.join(map(str, next(iter_cart))))
    print(' x '.join(map(str, next(iter_cart))))
    print()

    for product, quantity in cart_1:
        print(f'{product.name} by {product.price} UAH: {quantity}')
