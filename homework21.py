
def is_prime(func):
    def wrapper(*args):
        y = func(*args)
        for i in range(2,int (y / 2) + 1):
            if (y % i == 0):
                print('Составное')
                return y
        print("Просторе ")
        return y
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c
result = sum_three(2, 3, 6)
print(result)




