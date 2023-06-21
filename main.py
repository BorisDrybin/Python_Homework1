# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))

a = number // 100
b = (number % 100) // 10
c = number % 10

sum = a + b + c

print(f'Сумма цифр числа {number} равна {sum}')