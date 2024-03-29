"""
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

words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(words)

transformed_words = list()

for element in words:

    transformed_element = element.strip('+-')

    if transformed_element.isdigit():
        transformed_words.append('"')
        transformed_words.append(element.replace(transformed_element, transformed_element.zfill(2)))
        transformed_words.append('"')
    else:
        transformed_words.append(element)

print(transformed_words)


# Сформировать из обработанного списка строку
words_for_line = list()  # будем собирать слова в массив, экономим память
word_in_brackets = False  # флаг того, что скобки открылись

for element in transformed_words:
    words_for_line.append(element)

    if element == '"':
        word_in_brackets = not word_in_brackets  # мы должны понимать, открылась ли скобка, или закрылась

    if not word_in_brackets:
        words_for_line.append(" ")  # добавляем пробел Только когда мы не внутри скобок

line = ''.join(words_for_line)

print(line)
