'''
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
'''

from functools import wraps

def val_checker(check_func):
   def inner_checker(func):
      @wraps(func)
      def wrapped(num):
         if check_func(num):
            return func(num)
         else:
            raise ValueError(num)
      return wrapped
   return inner_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(5))
print(calc_cube(-5))
