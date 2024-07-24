def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


lst = [1,2,3,4,5]
print(sum_list(lst))