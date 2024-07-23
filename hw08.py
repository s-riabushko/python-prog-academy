# Task 1

def user_sequence(func, start_num, step, count):
    yield start_num
    n = start_num
    for _ in range(count - 1):
        user_command = input("Type any key for next number or 'exit': ")
        if user_command.lower().strip() == 'exit':
            break
        if func == '+':
            n = n + step
        elif func == '-':
            n = n - step
        elif func == '*':
            n = n * step
        elif func == '/':
            n = n / step
        else:
            raise ValueError(f'Invalid function {func}')
        yield n


user_func = input('Enter function(+ - * /): ')
user_start = int(input('Enter start number: '))
user_step = int(input('Enter step: '))
user_count = int(input('Enter count of numbers: '))
seq = user_sequence(user_func, user_start, user_step, user_count)
for item in seq:
    print(item)


# Task 2

import timeit

timeit_fibonacci = """
def fibonacci(num_count: int):
    a = 0
    b = 1
    for num in range(num_count - 2):
        a, b = b, b + a
    return b


fibonacci(20)
fibonacci(15)
fibonacci(25)
fibonacci(20)
fibonacci(10)
"""

timeit_fibonacci_mem = """
def fibonacci_mem():
    buf = [0, 1]

    def wrapper(n):
        if n < len(buf):
            return buf[n]

        a = buf[-2]
        b = buf[-1]
        for i in range(len(buf), n):
            a, b = b, b + a
            buf.append(b)
        return b

    return wrapper


fibonacci = fibonacci_mem()
fibonacci(20)
fibonacci(15)
fibonacci(25)
fibonacci(20)
fibonacci(10)
"""

print(timeit.repeat(timeit_fibonacci))
print(timeit.repeat(timeit_fibonacci_mem))


# Task 3
def sum_func(func):
    def wrapper(*args):
        return sum(func(*args))
    return wrapper


@sum_func
def user_func1(*args):
    return [arg * 2 for arg in args]


@sum_func
def user_func2(*args):
    return [arg ** 3 for arg in args]


res1 = user_func1(1, 2, 3, 4)
print(res1)
res2 = user_func2(1, 2, 3, 4)
print(res2)
