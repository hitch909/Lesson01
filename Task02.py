# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("введите трехзначное число  N =   "))
x = number % 10
y = number // 10 % 10
z = number // 100
summ = x + y + z
print(" сумма цифр из числа N = ", summ)

