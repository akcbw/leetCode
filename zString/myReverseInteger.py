from math import pow

"""
https://leetcode-cn.com/problems/reverse-integer/
"""


class Solution(object):
    def reverse(self, x):
        maxInteger = pow(2,31)
        if x == 0 or x < - maxInteger or x > maxInteger:
            return 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = abs(x)
        integerStack = []
        while x % 10 != x:
            outputDigit = x % 10
            integerStack.append(outputDigit)
            x = x // 10
        integerStack.append(x)

        sum = 0
        stackLength = len(integerStack)
        for i in range(stackLength):
            sum = sum + integerStack[i] * pow(10,stackLength - i - 1)
            if sum < - maxInteger or sum > maxInteger:
                return 0

        if isNegative:
            return - int(sum)
        return int(sum)

if __name__ == '__main__':
    print(Solution().reverse(-18618445646318684))
