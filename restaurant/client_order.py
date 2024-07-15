from restaurant.log import logger
from restaurant.dish import Dish
from restaurant.order import Order
from restaurant.discount import Discount


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
