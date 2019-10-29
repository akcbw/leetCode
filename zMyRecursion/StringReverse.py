"""
stringReverse(str) = str[-1] + stringReverse(str[:-1])

"""

from zStack.Stack import *

def strReverse(inputStr):
    if len(inputStr) == 1:
        return inputStr[-1]
    else:
        return inputStr[-1] + strReverse(inputStr[:-1])


def strReverseByStack(inputStr):
    st = MyStack()
    result = ''
    for c in inputStr:
        st.push(c)

    while not st.isEmpty():
        result = result + st.peek()
        st.pop()
    return result

def strReverseBySlice(inputStr):
    if inputStr is not None:
        return inputStr[::-1]
    return inputStr

if __name__ == "__main__":
    print(strReverse("Hellow World"))
    print(strReverseByStack("Hellow World22"))
    print(strReverseBySlice("Hellow World22"))