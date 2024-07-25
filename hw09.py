import datetime
import time


# Task 1
def decorator_1(func):
    def wrapper():
        print('Decorator before function')
        func()
        print('Decorator after function')
    return wrapper


@decorator_1
def my_func_1():
    print('\tmy_func body')


my_func_1()


# Task 2
def decorator_2(func):
    def wrapper(*args, **kwargs):
        f = open("res2.txt", "a")
        res = func(*args, **kwargs)
        f.write(f"{res}\n")
        f.close()
        return res
    return wrapper


@decorator_2
def calc_2(action, x, y):
    if action == '+':
        return x + y
    if action == '-':
        return x - y
    if action == '*':
        return x * y
    if action == '/':
        return x / y
    raise ValueError('allowed actions: + - * /')


res_2 = calc_2('*', 20, 50)
print(res_2)


# Task 3
def decorator_3(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
    return wrapper


@decorator_3
def calc_3(action, x, y):
    if action == '+':
        return x + y
    raise ValueError('allowed action: +')


res_3 = calc_3('*', 20, 50)
print(res_3)


# Task 4
def decorator_4(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        exec_time = time.time() - start_time
        print(f'Execution time: {exec_time} seconds')
        return res
    return wrapper


@decorator_4
def func_4(text):
    time.sleep(1.5)
    return text


res_4 = func_4('Hello')
print(res_4)


# Task 5
def decorator_5(func):
    def wrapper(*args, **kwargs):
        f = open("res5.txt", "a")
        current_time = datetime.datetime.now()
        f_args, f_kwargs = args, kwargs
        res = func(*args, **kwargs)
        f.write(f"{current_time}: {func.__name__} | {f_args} | {f_kwargs} | {res}\n")
        f.close()
        return res
    return wrapper


@decorator_5
def func_5_1(text, name='Ivan'):
    time.sleep(0.5)
    return f'{text}, {name}'


@decorator_5
def func_5_2(action, x, y):
    if action == '+':
        return x + y
    raise ValueError('allowed action: +')


res_5_1 = func_5_1('Hello')
res_5_2 = func_5_2('+', 50, 90)

print(res_5_1, res_5_2)


# Task 6
def decorator_6_wrap(exec_limit):
    def decorator_6(func):
        exec_count = 0

        def wrapper(*args, **kwargs):
            nonlocal exec_count
            if exec_count >= exec_limit:
                raise RuntimeError('function call limit reached')
            exec_count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator_6


@decorator_6_wrap(3)
def calc_6(action, x, y):
    print(x, action, y)


calc_6('+', 20, 50)
calc_6('+', 20, 50)
calc_6('+', 20, 50)
calc_6('+', 20, 50)
