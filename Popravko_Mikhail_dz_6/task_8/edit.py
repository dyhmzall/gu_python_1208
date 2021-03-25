import sys
import sales

summa_number = int(sys.argv[1]) if len(sys.argv) > 1 else None
summa = sys.argv[2] if len(sys.argv) > 2 else None

if summa_number and summa:
    sales.edit_summa(summa_number, summa)
else:
    print("Запустите скрипт с параметрами, например: python edit.py 5 100.01")
