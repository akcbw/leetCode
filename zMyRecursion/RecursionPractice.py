# -*- coding:utf-8-*-
# 将 10不断除以2，直至商为0，输出这个过程中每次得到的商的值。
import sys
sys.setrecursionlimit(100000)

def recursion(n):
    v = n//2 # 地板除，保留整数
    #print(v) # 每次求商，输出商的值
    if v==0:
        ''' 当商为0时，停止，返回Done'''
        return 'Done'
    v = recursion(v) # 递归调用，函数内自己调用自己

recursion(19)


# 1！+2！+3！+4！+5！+...+n!
def sum(n):
    result = 0
    for i in range(1, n+1):
        def factorial(n):
            if n == 1:
                return n
            m = n * factorial(n-1)
            return m
        if n == 1:
            return n
    result = result +  factorial(n)
    return result

print(sum(4))

def sum2(n):
    if n == 1:
        return 1
    n = n + sum2(n-1)
    return n
print(sum2(5))