class ProductPriceError(Exception):
    def __init__(self, message='Product price value error'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Price cannot be less or equals zero'
