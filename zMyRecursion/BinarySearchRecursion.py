def binarySearchRecursion(searchArray, start, end,item):
    subArray = searchArray[start: end]
    minIndex = len(subArray) // 2
    if subArray[minIndex] == item:
        return minIndex + start
    elif minIndex == 0:
        return None
    else:
        if subArray[minIndex] > item:
            return binarySearchRecursion(searchArray,start, end - minIndex, item)
        elif subArray[minIndex] < item:
            return binarySearchRecursion(searchArray, start + minIndex, end, item)
searchArray = [0, 1, 2, 8, 13, 17, 19, 32, 78]

print(binarySearchRecursion(searchArray, 0, len(searchArray), 100))
print(binarySearchRecursion(searchArray,0, len(searchArray),17))


def binarySearchNonRecursion(searchArray, item):
    i = len(searchArray)//2
    start = 0
    end = len(searchArray)-1
    while start <= end:
        if searchArray[i] == item:
            return i
        elif searchArray[i] < item:
            start = i + 1
            i = start + (end - start)//2
        else:
            end = i - 1
            i = end // 2
    return None
print(binarySearchNonRecursion(searchArray, 100))
print(binarySearchNonRecursion(searchArray,17))
