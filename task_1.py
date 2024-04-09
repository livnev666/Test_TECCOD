# task_1


def set_integers(lst: list):

    lst_2 = []
    a = set(lst)
    for i in a:
        lst_2.append(i)
    return lst_2


print(set_integers([1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8]))