"""
Use recursion to calculation sum of array elements
Equation:
sumOfArray(numList)=first(numList)+sumOfArray(rest(numList))
"""
def sumOfArray(numberArr):
    if len(numberArr) == 1:
        return numberArr[0]
    else:
        return numberArr[0] + sumOfArray(numberArr[1:])


"""
Use recursion to calculation sum of array elements
Equation:
sumOfArray(numList)=last(numList)+sumOfArray(revious(numList))
"""
def sumOfArray2(numberArr):
    if len(numberArr) == 1:
        return numberArr[-1]
    else:
        return sumOfArray2(numberArr[:-1]) + numberArr[-1]


if __name__ == '__main__':
    print(sumOfArray([8]))
    print(sumOfArray2([8]))