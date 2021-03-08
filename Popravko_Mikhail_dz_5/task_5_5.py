"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

uniq = set()
double = set()

for num in src:
    if num not in uniq:
        uniq.add(num)
    else:
        double.add(num)

result = uniq - double

print(result)  # уникальные значения

sorted_result = (el for el in src if el in result)

print(*sorted_result)  # у никальные значения в правильном порядке
