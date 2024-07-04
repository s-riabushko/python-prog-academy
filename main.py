# Task 1

class ProductPriceError(Exception):
    def __init__(self, message='Product price value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Price cannot be less or equals zero'


class Product:
    def __init__(self, name: str, price: int | float):
        if not isinstance(price, int | float):
            raise TypeError("Price must be 'int' or 'float'")
        if price <= 0:
            raise ProductPriceError("Price can't be less than zero")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


class Cart:

    def __init__(self):
        self.__products = {}

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
            raise TypeError("Invalid quantity type, must be 'int' or 'float'")
        if quantity < 0:
            raise ValueError("Quantity can't be less than zero")

        self.__products[product] = self.__products.get(product, 0) + quantity

    def clear_cart(self):
        """
        Remove all products from the cart.
        :return: None
        """
        self.__products.clear()

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


pr_1 = Product("Bread", 10)
pr_2 = Product("Milk", 20)
pr_3 = Product("Butter", -1)

cart_1 = Cart()
cart_1.add_product(pr_1, 2)
cart_1.add_product(pr_2, 3)
cart_1.add_product(pr_3)
cart_1.add_product(pr_3, 3)

print(cart_1)


# Task 2

class Dish:
    def __init__(self, name: str, price: int | float):
        if not isinstance(price, int | float):
            raise TypeError("Price must be 'int' or 'float'")
        if price < 0:
            raise ValueError("Price can't be less than zero")
        self.name = name
        self.price = price

    def __str__(self):
        return f'  {self.name}: {self.price}$'


class Order:
    def __init__(self):
        self.__dishes = {}

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
            raise TypeError('Quantity must be integer')
        if quantity < 1:
            raise ValueError('Quantity must grater then zero')

        self.__dishes[dish] = self.__dishes.get(dish, 0) + quantity

    def remove_dish(self, dish: Dish):
        """
        Remove dish from the order.
        :param dish: Dish object
        :return: None
        """
        if not isinstance(dish, Dish):
            raise TypeError('Invalid dish object')

        if dish not in self.__dishes:
            raise ValueError('Dish not in the category')

        self.__dishes.pop(dish)

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


class DiscountValueError(Exception):
    def __init__(self, message='Discount value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Discount value must be greater than 0 and less than 100'


class Discount:
    def __init__(self, discount_val: int | float = 0):
        if not isinstance(discount_val, int | float):
            raise TypeError("Discount value must be 'int' or 'float'")
        if discount_val < 0 or discount_val > 100:
            raise DiscountValueError()
        self.discount_val = discount_val

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


def main():
    tomato_soup = Dish('Tomato soup', 10)
    onion_soup = Dish('French onion soup', 15)
    salad = Dish('Chicken Salad', 10)
    omelette = Dish('Cheese omelette', 20)
    burger = Dish('Burger', 30)
    sandwich = Dish('Chicken sandwich', 20)

    order1 = Order()
    order1.add_dish(onion_soup, 1)
    order1.add_dish(sandwich, 2)
    order1.add_dish(salad, 2)
    order1.add_dish(omelette, 2)
    order1.add_dish(salad)

    client_discount = float(input('Enter your discount(%): '))
    discount = Discount(client_discount)
    client1 = ClientOrder('Ivan', order1, discount)

    print(client1)


if __name__ == '__main__':
    main()
