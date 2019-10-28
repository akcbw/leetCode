from zStack import Stack

def stringParenthesisChecker(inputStri):
    st = Stack.MyStack()
    for s in inputStri:
        if s == "(":
            st.push(s)
        elif s == ")":
            if st.isEmpty():
                return False
            else:
                st.pop()

    return st.isEmpty()

print("Test is parenthese")
print(stringParenthesisChecker("((((((((((fdsfs(2ff)"))
