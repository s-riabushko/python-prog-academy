import cart
import restaurant


def main():

    # Task 1
    try:
        pr_1 = cart.Product("Bread", 10)
        pr_2 = cart.Product("Milk", 20)
        pr_3 = cart.Product("Butter", 1)

        cart_1 = cart.Cart()
        cart_1.add_product(pr_1, 2)
        cart_1.add_product(pr_2, 3)
        cart_1.add_product(pr_3)
        cart_1.add_product(pr_3, 3)

        print(cart_1)

    except cart.ProductPriceError as e:
        print(e)

    # Task 2
    try:
        onion_soup = restaurant.Dish('French onion soup', 15)
        salad = restaurant.Dish('Chicken Salad', 10)
        omelette = restaurant.Dish('Cheese omelette', 20)
        sandwich = restaurant.Dish('Chicken sandwich', 20)

        order1 = restaurant.Order()
        order1.add_dish(onion_soup, 1)
        order1.add_dish(sandwich, 2)
        order1.add_dish(salad, 2)
        order1.add_dish(omelette, 2)
        order1.add_dish(salad)

        client_discount = float(input('Enter your discount(%): '))
        discount = restaurant.Discount(client_discount)
        client1 = restaurant.ClientOrder('Ivan', order1, discount)

        print(client1)

    except restaurant.DiscountValueError as e:
        print(e)


if __name__ == '__main__':
    main()
