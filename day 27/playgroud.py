def add(*args):
    """ args (arguments) will give return type as tuple """
    count = 0
    for i in args:
        count += i
    print(count)


add(5, 6)


def calculate(n, **kwargs):
    """ kwargs (keyword arguments) will give a return type as dictionary """
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
