'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
 odd_to_15 = odd_nums(15)
 next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
'''

def odd_generator(n):
    for x in range(1, n + 1):
        if x % 2 != 0:
            yield x

odd_gen1 = odd_generator(50)
print(*odd_gen1)

max_range = 75
odd_gen2 = (x for x in range(1, max_range + 1) if x % 2 != 0)
print(*odd_gen2)

