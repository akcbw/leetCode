def findMinimumIndexSum(list1, list2):
    if list1 is None or list2 is None:
        return None
    elif len(list1) < 2 or len(list2) < 2:
        return list1
    else:
        map = dict()
        keyList = []
        for element1 in list1:
            if element1 in list2:
                key = list1.index(element1) + list2.index(element1)
                keyList.append(key)
                map[element1] = key

    keyList.sort()

    for k,v in map.items():
        if v == keyList[0]:
            print(k)


if __name__ == '__main__':
    list = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    list3 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list4 = ["KFC","Burger King","Tapioca Express", "Shogun"]
    findMinimumIndexSum(list3, list4)