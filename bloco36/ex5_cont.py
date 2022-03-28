# Consulte a forma de se criar um dicionário chamado de dict comprehension
#  e crie um dicionário que mapeia inteiros de 3 a 20 para o seu dobro.

my_dict = {num: num * 2 for num in range(3, 21)}


if __name__ == "__main__":

    print(my_dict)
