import shop.product as shop_product
import shop.cart as shop_cart
import shop.cart_exception as shop_exception

import restaurant.dish as rest_dish
import restaurant.order as rest_order
import restaurant.discount as rest_discount
import restaurant.client_order as rest_client_order
import restaurant.restaurant_exception as rest_exception
import time

from rational import Rational


def main():
    # Task 1
    print("Task 1")
    try:
        pr_1 = shop_product.Product("Bread", 10)
        pr_2 = shop_product.Product("Milk", 20)
        pr_3 = shop_product.Product("Butter", 30)
        pr_4 = shop_product.Product("Olive oil", 25)
        pr_5 = shop_product.Product("Sausage", 50)
        cart_1 = shop_cart.Cart()
        cart_1.add_product(pr_1, 2)
        cart_1.add_product(pr_2, 3)
        cart_1.add_product(pr_3, 2)
        cart_2 = shop_cart.Cart()
        cart_2.add_product(pr_3, 3)
        cart_2.add_product(pr_4, 2)
        cart_2.add_product(pr_5, 2)
        print(cart_1, '\n')
        print(cart_2, '\n')
        cart_1 += cart_2
        print(cart_1, '\n')
    except shop_exception.ProductPriceError as e:
        print(e)
    except Exception as e:
        print(e)

    # Task 2
    print("Task 2")
    try:
        onion_soup = rest_dish.Dish('French onion soup', 15)
        salad = rest_dish.Dish('Chicken Salad', 10)
        omelette = rest_dish.Dish('Cheese omelette', 20)
        sandwich = rest_dish.Dish('Chicken sandwich', 20)
        order1 = rest_order.Order()
        order1.add_dish(onion_soup, 2)
        order1.add_dish(sandwich, 1)
        order1 += sandwich
        order1 += omelette
        order1 += salad
        time.sleep(0.2)
        client_discount = float(input('Enter your discount(%): '))
        discount = rest_discount.Discount(client_discount)
        client1 = rest_client_order.ClientOrder('Ivan', order1, discount)
        print(client1)
    except rest_exception.DiscountValueError as e:
        print(e)
    except rest_exception.PriceValueError as e:
        print(e)
    except Exception as e:
        print(e)
    time.sleep(0.2)

    # Task 3
    print("\nTask 3")
    x = Rational(3, 11)
    y = Rational(7, 8)
    print(x < y)
    print(x + y)
    print(x - y)
    print(x * y)


if __name__ == '__main__':
    main()
