"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(callback_func):
    def _checker(func):
        def wrapper(*args, **kwargs):
            if not callback_func(args[0]):
                raise ValueError(f"wrong val {args[0]}")
            return func(*args, **kwargs)

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
