def split_pairs(a):
    list = []
    n = 2
    for i in range(0, len(a), n):
        pice_of_a = a[i:i+n]
        if len(pice_of_a) % 2 == 0: list.append(pice_of_a)
        else: list.append(f'{pice_of_a}_')
    return list