#!/usr/bin/python3 chmod 777 *.py
# print("Hello World")
# x = input("Année: ")
# y = int(x) + 1
# print(y)
# print(f"L'année est {y}")
# print("L'année est "+str(y))
# if y % 2 == 0:
#     print("Pair")
# else:
#     print("Impair")

# for i in range(10,-1,-1):
#     print(i)

def isPrime(x):
    res = True
    for i in range(2, x):
        if x % i == 0:
            res = False
            break
    return res

print(isPrime(2731))
print(isPrime(2732))
