#Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так, например:
#def val_checker...
#    ...\
#@val_checker(lambda x: x > 0)
#def calc_cube(x):
#   return x ** 3
#>>> a = calc_cube(5)
#125
#>>> a = calc_cube(-5)
#Traceback (most recent call last):
#  ...
#    raise ValueError(msg)
#ValueError: wrong val -5

from functools import wraps

def val_checker(func):
    def _val_checker(f_calc_cube):
        @wraps(f_calc_cube)
        def wrapped(x):
            if func(x):
                return f_calc_cube(x)
            else:
                raise ValueError(x)
        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5))