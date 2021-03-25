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
