from datetime import date, timedelta  # used in Task 6


# Task 1
def geometric(n: int):
    """
    Function for return each term of a geometric progression
    :param n: number of terms of a geometric progression
    :return: integer
    """
    x = 1
    yield x
    for item in range(1, n+1):
        x = x * (item + 1)
        yield x


# Task 2
def my_range(*args: int):
    """
    Analog of built-in function ragne()
    :param args: (stop), (start, stop) or (start, stop, step). For step can be used negative value.
    :return: range of integer numbers
    """
    if not len(args) or len(args) > 3:
        msg = f'my_range() takes either 1, 2 or 3 arguments, {len(args)} given'
        raise TypeError(msg)
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError('Only integers can be specified')

    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
        if step == 0:
            raise ValueError("Step cannot be equal of zero")

    if start < 0 or stop < 0:
        raise ValueError("'start' and 'stop' can be only positive integers")
    if start > stop:
        raise ValueError("'start' cannot be greater then 'stop'")

    if step < 0:
        start, stop = stop - 1, start - 1
    range_num = start
    while range_num != stop:
        if step > 0 and range_num >= stop or step < 0 and range_num <= stop:
            break
        yield range_num
        range_num += step


# Task 3
def prime_numbers(end_num: int):
    """
    Function to find and return every prime number
    :param end_num: max value to search for prime numbers.
    :return: range of prime numbers
    """
    if not isinstance(end_num, int):
        raise TypeError('num_count can be only integer')
    if end_num <= 0:
        raise ValueError('num_count can be only positive integer')

    for prime_num in range(2, end_num + 1):
        for i in range(2, prime_num):
            if (prime_num % i) == 0:
                break
        else:
            yield prime_num


# Task 4
# function range() is used


# Task 5
def fibonacci(num_count: int):
    """
    Returns the given number of Fibonacci numbers
    :param num_count: count of Fibonacci numbers
    :return: range of Fibonacci numbers starts from 0 to num_count
    """
    if not isinstance(num_count, int):
        raise TypeError('num_count can be only integer')
    if num_count <= 0:
        raise ValueError('num_count can be only positive integer')
    a = 0
    yield a
    b = 1
    yield b
    for num in range(b, num_count - 1):
        a, b = b, b + a
        yield b


# Task 6
def dates(start_date: str, end_date: str):
    """
    Returns every date in a given range
    :param start_date: start date in ISO format
    :param end_date: end date in ISO format
    :return: every date in a given range
    """
    date.fromisoformat(start_date)
    date.fromisoformat(end_date)
    yield start_date
    step = 1
    end = start_date
    while end != end_date:
        end = str(date.fromisoformat(end) + timedelta(days=step))
        yield end


def main():
    print(f"\n# Task 1:")
    num_len = 4
    x = geometric(num_len)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

    print(f"\n# Task 2:")
    for item in my_range(11, 18):
        print(item)

    print(f"\n# Task 3:")
    prime_len = 100
    prime_num = [item for item in prime_numbers(prime_len)]
    print(prime_num)

    print(f"\n# Task 4:")
    list_len = 25
    cube_list = [item ** 3 for item in range(list_len)]
    print(cube_list)

    print(f"\n# Task 5:")
    num_len = 20
    fibonacci_list = [item for item in fibonacci(num_len)]
    print(fibonacci_list)

    print(f"\n# Task 6:")
    start_date = '2024-07-18'
    end_date = '2024-07-21'
    date_list = [item for item in dates(start_date, end_date)]
    print(date_list)


if __name__ == '__main__':
    main()
