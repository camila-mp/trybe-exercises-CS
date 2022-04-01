# Escreva uma função que identifique o único número duplicado em uma lista.
# Retorne o número duplicado em O(n).


def find_duplicated_num(list):
    numbers = []
    for num in list:
        if num not in numbers:
            numbers.append(num)
        if num in numbers:
            return num


print(find_duplicated_num([1, 3, 2, 4, 5, 1]))
