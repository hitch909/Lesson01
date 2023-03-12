# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("введите трехзначное число  N =   "))
#x = number % 10
#y = number // 10 % 10
#z = number // 100
#summ = x + y + z
#print(" сумма цифр из числа N = ", summ)

# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("введите любое целое число  N =   "))


def sum_of_digits(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    return summ


print(sum_of_digits(number))

