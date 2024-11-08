def concat_lists(list1: list, list2: list) -> list:
    list3 = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            list3.append(list1[i])
        if i < len(list2):
            list3.append(list2[i])
    return list3
print(concat_lists([1, 2, 3], [3, 2, 1]))
