from abc import ABC, abstractmethod
import math


# Task 1
class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):

    def __init__(self, radius: int | float):
        self.radius = radius

    def perimeter(self):
        res = 2 * math.pi * self.radius
        return res

    def area(self):
        res = math.pi * self.radius ** 2
        return res

    def __str__(self):
        return (f"Circle with radius {self.radius}\n"
                f"Perimeter: {self.perimeter():.2f}\nArea: {self.area():.2f}")


class Triangle(Figure):

    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        res = self.side_a + self.side_b + self.side_c
        return res

    def area(self):
        p = self.perimeter() / 2
        res = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return res

    def __str__(self):
        return (f"Triangle with sides: {self.side_a}, {self.side_b}, {self.side_c}.\n"
                f"Perimeter: {self.perimeter()}\nArea: {self.area():.2f}")


class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        res = (self.side_a + self.side_b) * 2
        return res

    def area(self):
        res = self.side_a * self.side_b
        return res

    def __str__(self):
        return (f"Rectangle with sides: {self.side_a}, {self.side_b}, {self.side_a}, {self.side_b}.\n"
                f"Perimeter: {self.perimeter()}\nArea: {self.area()}")


x = Circle(15)
print(x)
y = Triangle(10, 20, 30)
print(y)
z = Rectangle(10, 20)
print(z)


# Task 2
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f'Paying {amount} using Credit Card')


class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f'Paying {amount} using Bank Transfer')


class OnlineWallet(PaymentMethod):
    def pay(self, amount):
        print(f'Paying {amount} Online Wallet')


class PaymentProcessor:
    def __init__(self, amount: int | float, payment_method: PaymentMethod):
        self.amount = amount
        self.payment_method = payment_method
        self.__payment_methods = [cls.__name__ for cls in PaymentMethod.__subclasses__()]

    def make_payment(self):
        self.payment_method.pay(self, self.amount)

    def __str__(self):
        return f"Allowed payment methods: {', '.join(map(str, self.__payment_methods))}"


credit_card = CreditCard
bank_transfer = BankTransfer
online_wallet = OnlineWallet

need_pay = PaymentProcessor(150, credit_card)
need_pay.make_payment()

need_pay = PaymentProcessor(300, bank_transfer)
need_pay.make_payment()

print(need_pay)