
class Discount:
    def discount(self):
        pass


class RegularDiscount(Discount):
    def discount(self):
        return 0.05


class SilverDiscount(Discount):
    def discount(self):
        return 0.1


class GoldDiscount(Discount):
    def discount(self):
        return 0.2


class Client:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        return order - order * self.discount.discount()


def main():
    gold_discount = GoldDiscount()
    silver_discount = SilverDiscount()
    regular_discount = RegularDiscount()

    client1 = Client('Ivan', regular_discount)
    client2 = Client('Petro', silver_discount)
    client3 = Client('Pavlo', gold_discount)
    client4 = Client('Stepan', gold_discount)
    client5 = Client('Bogdan', regular_discount)
    print(client1.get_total_price(100))
    print(client2.get_total_price(200))
    print(client3.get_total_price(500))
    print(client4.get_total_price(200))
    print(client5.get_total_price(300))


if __name__ == '__main__':
    main()
