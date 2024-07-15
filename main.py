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

    try:
        pr_1 = shop_product.Product("Bread", 10)
        pr_2 = shop_product.Product("Milk", 20)
        pr_3 = shop_product.Product("Butter", 30)
        pr_4 = shop_product.Product("Olive oil", 25)
        cart_1 = shop_cart.Cart()
        cart_1.add_product(pr_1, 2)
        cart_1.add_product(pr_2, 3)
        cart_1.add_product(pr_3, 2)
        cart_2 = shop_cart.Cart()
        cart_2.add_product(pr_3, 3)
        cart_2.add_product(pr_4, 2)
        cart_1 += cart_2

        # Task 1
        iter_cart = iter(cart_1)
        print(' x '.join(map(str, next(iter_cart))))
        print(' x '.join(map(str, next(iter_cart))))
        print(' x '.join(map(str, next(iter_cart))))
        print(' x '.join(map(str, next(iter_cart))))
        print()

        for product, quantity in cart_1:
            print(f'{product.name} by {product.price} UAH: {quantity}')
        # end of Task 1

    except shop_exception.ProductPriceError as e:
        print(e)
    except Exception as e:
        print(e)

    try:
        onion_soup = rest_dish.Dish('French onion soup', 15)
        salad = rest_dish.Dish('Chicken Salad', 10)
        omelette = rest_dish.Dish('Cheese omelette', 20)
        sandwich = rest_dish.Dish('Chicken sandwich', 20)
        order1 = rest_order.Order()
        order1.add_dish(omelette, 2)
        order1.add_dish(onion_soup, 3)
        order1.add_dish(salad, 1)
        order1.add_dish(sandwich, 1)

        # Task 2
        iter_order = iter(order1)
        print(' x '.join(map(str, next(iter_order))))
        print(' x '.join(map(str, next(iter_order))))
        for dish, quantity in order1:
            print(f'{dish} X {quantity}')

        order1_rev = order1[::-1]
        print(type(order1_rev))
        print('\n'.join(map(lambda item: f'{item[0].name}: {item[1]}', order1_rev)))
        # end of Task 2

        client_discount = 15
        discount = rest_discount.Discount(client_discount)
        client1 = rest_client_order.ClientOrder('Ivan', order1, discount)
        print(client1)
    except rest_exception.DiscountValueError as e:
        print(e)
    except rest_exception.PriceValueError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
