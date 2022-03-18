# Dado um array com os seguintes elementos ["zebra", "macaco", "elefante", "arara", "javali"] , após duas iterações utilizando bubble sort , como estaria este array?
def zoo_bubble_sort(array):
    has_swapped = True
    num_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(array) - num_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_iterations += 1
    return array


arr = ["zebra", "macaco", "elefante", "arara", "javali"]
print(zoo_bubble_sort(arr))

# macaco zebra elefante arara javali

# macaco elefante zebra arara javali

# macaco elefante arara zebra javali

# macaco elefante arara javali zebra

# 1 iteration

# elefante macaco arara javali zebra

# elefante arara macaco javali zebra

# elefante arara javali macaco zebra

# elefante arara javali macaco zebra

# 2 iterations
