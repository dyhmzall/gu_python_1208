"""
3. Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""

plural_list = ['процент', 'процентов', 'процента']

for number in range(21):
    if number == 1:
        plural = plural_list[0]
    elif 2 <= number <= 4:
        plural = plural_list[2]
    else:
        plural = plural_list[1]

    print(number, plural)
