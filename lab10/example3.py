def sum_list(l):
    if len(l)==0:
        return []

    if isinstance(l[0],list):
        return sum_list(l[0]) + sum_list(l[1:])

    return (l)[:1] + sum_list(l[1:])


print(sum(sum_list([3,12,76,[4,56,43],[2,8],81,75])))