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
