"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
Внимание: новый список не создавать!!!
"""

divider = 7
additional_number = 17

sum_divider = 0
sum_additional_divider = 0

odd_list = []

for el in range(1, 1000, 2):

    original_number = el ** 3
    odd_list.append(original_number)

    # это число будет делить каждый раз на 10, чтобы получить сумму цифр
    number = original_number
    sum_digit = 0

    while number:
        sum_digit += number % 10
        number //= 10

    if not sum_digit % divider:
        sum_divider += original_number

    # применим тот же алгоритм, функцию не использую, так как мы их еще не проходили
    number = original_number + additional_number
    sum_digit = 0

    while number:
        sum_digit += number % 10
        number //= 10

    if not sum_digit % divider:
        sum_additional_divider += original_number

print(f"Список кубов нечетных числе от 0 до 100: {odd_list}")
print(f"Сумма тех чисел, сумма цифр которых делится на {divider} составляет {sum_divider}")
print(f"Сумма тех чисел, сумма цифр которых делится на {divider} составляет {sum_additional_divider}")
