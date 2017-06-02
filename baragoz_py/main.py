# n = input("Факториал числа ")
# n = int(n)
# fac = 1
# i = 0
# while i < n:
#      i += 1
#      fac = fac * i
# print ("равен",fac)

"""Функция проверки числа на простоту"""
# def is_prime(x):
#     if x > 3 and x % 2 == 0 or x <= 1:
#         return False
#     for i in range(3, int(x ** 0.5) + 1, 2):
#         if x % i == 0:
#             return False
#     return True
# summ=0

import pickle




def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper

@benchmark
def is_prime(n):
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
        i += 1
    # print(lst)
    f = open("out.txt", "wb")
    f.write(pickle.dumps(lst))
    f.close()
    # print(len(lst))

is_prime(1000000)
# for i in range(100000,1000000):
#      if is_prime(i):
#           summ+=1
# print(summ)