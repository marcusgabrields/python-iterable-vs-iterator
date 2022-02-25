minha_string = "python"
meu_iterador = iter(minha_string)  # 1
while True:
    try:
        print(next(meu_iterador))  # 2
    except StopIteration:  # 3
        del meu_iterador  # 4
        break  # 5

# p
# y
# t
# h
# o
# n
