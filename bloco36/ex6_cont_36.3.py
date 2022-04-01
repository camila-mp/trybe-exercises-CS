# Dada uma string, construa um dicionário com a contagem de
# cada caractere da palavra. Utilize o pseudocódigo para se nortear.

# Dica:
# Para cada char na string:
#     - Se o char não estiver no dicionário, inclua com o valor 1;

#     - Se estiver, incremente o valor.


def number_chars_dict(a_string):

    string_dict = {}

    for char in list(a_string):
        if char not in string_dict.keys():
            string_dict[char] = 1
        elif char in string_dict.keys():
            string_dict[char] += 1
    return string_dict


my_string = "coxinha"

assert (number_chars_dict(my_string)) == {
    "c": 1,
    "o": 1,
    "x": 1,
    "i": 1,
    "n": 1,
    "h": 1,
    "a": 1,
}
