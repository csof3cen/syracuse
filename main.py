def syracuse(nbre_de_depart=1, nbre_iteration=2):
    next_number = nbre_de_depart

    if isinstance(nbre_de_depart, int):
        for i in range(nbre_iteration):
            if next_number % 2 == 0:
                next_number //= 2
            else:
                next_number = next_number * 3 + 1

            print(next_number)


syracuse(1, 15)
