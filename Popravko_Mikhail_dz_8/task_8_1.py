"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
"""

import re

# используем предварительую компиляцию, потому что проверка для всех email всегда будет одна и та же
# и потенциально может пригодиться не только в функции email_parse(), но и где-то еще
# используем упрощенную версию проверки (грубо говорят что есть что-то перед @ и после что-то похожее на доменное имя)
RE_EMAIL = re.compile(r"^(\w+)@([a-zA-Z0-9\-]+\.[a-zA-Z]+)$")


def email_parse(email):
    if not RE_EMAIL.match(email):
        raise ValueError(f"wrong email: {email}")
    search = RE_EMAIL.search(email)
    return {
        "username": search.group(1),
        "domain": search.group(2)
    }


email_for_test = [
    "test@test.ru",
    "my@my.com",
    "12@gmail.com",
    "vk.ru"
]

for email in email_for_test:
    try:
        email_dict = email_parse(email)
    except ValueError as e:
        print(email, " - ", e)
    else:
        print(email, " - ", email_dict)
