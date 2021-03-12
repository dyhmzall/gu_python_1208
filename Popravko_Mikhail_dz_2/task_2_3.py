"""
3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.

2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
"""

words_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(words_list)

index = 0

while True:

    element = words_list[index]
    element = element.strip('+-')

    if element.isdigit():

        if index == 0:  # если массив начинается с цифры - сместим массив, чтобы влезла левая скобка
            words_list.insert(index, '')
            index += 1

        words_list[index] = words_list[index].replace(element, element.zfill(2))
        words_list.insert(index, '"')
        words_list.insert(index + 2, '"')

        index += 2  # так как мы вставили 2 элемента, индекс смещаем на 2 в дополнение к каждому шагу

    if index < len(words_list) - 1:
        index += 1  # перебираем индексы
    else:
        break

print(words_list)


# Сформировать из обработанного списка строку
transformed_words_list = list()  # будем собирать слова в массив, экономим память
word_in_brackets = False  # флаг того, что скобки открылись

for element in words_list:
    transformed_words_list.append(element)

    if element == '"':
        word_in_brackets = not word_in_brackets  # мы должны понимать, открылась ли скобка, или закрылась

    if not word_in_brackets:
        transformed_words_list.append(" ")  # добавляем пробел Только когда мы не внутри скобок

line = ''.join(transformed_words_list)

print(line)