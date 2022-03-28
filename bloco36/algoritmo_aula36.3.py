# Dado um array de tuplas que contem pares de pessoas em uma fila, onde a
# segunda pessoa (index [0]) está na frente da primeira,
# retorne um array com a ordem das pessoas na fila.


def get_order(orders):
    orders_map = {pair[0]: pair[1] for pair in orders}
    # print(orders_map)

    next_person = ""
    for person in orders_map:  # iterates over keys NOT VALUES

        if person not in orders_map.values():
            next_person = person
    result = [next_person]

    while next_person in orders_map:

        result.append(orders_map[next_person])
        next_person = orders_map[next_person]
    return result


if __name__ == "__main__":
    orders = [
        ("fernanda", "rafa"),
        ("fran", "daniel"),
        ("mirian", "gabriel"),
        ("matheus", "yasmin"),
        ("giovanni", "fernanda"),
        ("rafa", "fran"),
        ("daniel", "mirian"),
        ("gabriel", "matheus"),
    ]

    assert get_order(orders) == [
        "giovanni",
        "fernanda",
        "rafa",
        "fran",
        "daniel",
        "mirian",
        "gabriel",
        "matheus",
        "yasmin",
    ]
    print(get_order(orders))
