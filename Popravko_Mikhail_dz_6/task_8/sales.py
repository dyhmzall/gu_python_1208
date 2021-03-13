from itertools import islice

SUMMA_FILENAME = "summa.csv"


def add_summa(summa):
    with open(SUMMA_FILENAME, "a", encoding="utf-8") as f:
        f.write(summa + "\n")


def get_summa_generator():
    with open(SUMMA_FILENAME, "r", encoding="utf-8") as f:
        for summa in f:
            yield summa.strip()


def get_summa_for_show(from_number, to_number):
    for i, summa in enumerate(islice(get_summa_generator(), from_number, to_number), from_number + 1):
        yield i, summa


def edit_summa(summa_number, summa_new):
    print(summa_number, summa_new)

    with open(SUMMA_FILENAME, "r+", encoding="utf-8") as f:

        i = 1  # счетчик, показывает, какая по счету текущая строка
        while True:
            summa = f.readline()
            if summa is None:
                exit(1)  # ситуация, когда указали неверный номер
            if i == summa_number:
                f.seek(f.tell() - len(summa) - 1)  # установим курсок на начало строки
                f.write(summa_new + "\n")
                # если мы перетерли не все данные, заполним старые данные пробелами
                # например если было 1000.00 а пишем 10.00
                diff = len(summa) - len(summa_new)
                if diff > 0:
                    f.write(' ' * diff)
                break
            i += 1
