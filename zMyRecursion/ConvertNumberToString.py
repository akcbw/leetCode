"""
decimal scenario:

convertNumToString(number) = convertNumberToString(number//10) + strDic[number % 10]

"""

def convertNumToString(number):
    strDic = "0123456789"
    if number//10 == 0:
        return strDic[number]
    else:
        return convertNumToString(number // 10) + strDic[number % 10]

"""
support different base scenario:

base could be 2, 10 ,8, 16

convertNumToString(number,base) = convertNumberToString(number//base, base) + strDic[number % base]

"""

def convertNumToStringDiffBase(number, base):
    strDic = "0123456789ABCDEF"
    if number//base == 0:
        return strDic[number]
    else:
        return convertNumToStringDiffBase(number // base, base) + strDic[number % base]


if __name__ == '__main__':
    print(convertNumToString(10))
    print(convertNumToStringDiffBase(10, 2))
    print(convertNumToStringDiffBase(10, 8))
    print(convertNumToStringDiffBase(10, 16))