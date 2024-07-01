my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec(n):
    if len(n) != 0:
        print(my_list[0])
        my_list.pop(0)
        rec(n)
    else: (print("Конец списка"))

rec(my_list)
