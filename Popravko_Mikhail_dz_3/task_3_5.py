"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
from random import choice


def get_jokes(joke_count=1, repeat=True):
    """Получить N шуток, каждая из которых будет состоять из 3х слов"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = list()

    for i in range(joke_count):

        first_word = choice(nouns)
        if not repeat:
            nouns.remove(first_word)

        second_word = choice(adverbs)
        if not repeat:
            adverbs.remove(second_word)

        third_word = choice(adjectives)
        if not repeat:
            adjectives.remove(third_word)

        jokes.append(' '.join([first_word, second_word, third_word]))

    return jokes


print(get_jokes())
print(get_jokes(2))
print(get_jokes(3))
print(get_jokes(joke_count=4, repeat=False))
print(get_jokes(joke_count=5, repeat=False))

