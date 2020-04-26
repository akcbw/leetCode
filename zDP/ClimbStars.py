
def climbStairs(n):
    dpTable = []
    for i in range(n):
        if i < 2:
            dpTable.append(i+1)
        else:
            dpTable.append(dpTable[i-1] + dpTable[i-2])
    return dpTable[i]

def climbStairsDP(n):
    dpTable = []
    for i in range(n):
        if n < 2:
            dpTable.append(n + 1)
        else:
            dpTable.append(dpTable[n-1] + dpTable[n-2])
    return dpTable[n]

def climbStairsDP2(n, stairRange):
    dpTable = [0] * n
    for i in range(n):
        for j in stairRange:
            if i > j:
                dpTable[n] = dpTable[n] + dpTable[n - j]
    return dpTable[n]

def climStairsRecursion(n):
    if n < 3:
        return n
    else:
        return climStairsRecursion(n - 2) + climStairsRecursion(n - 1)

def climbStarsRecursionWithMemory(n, memory):
    if n < 3:
        memory[n] = n
        return n
    elif n in memory:
        return memory[n]
    else:
        return climbStarsRecursionWithMemory(n-2, memory) + climbStarsRecursionWithMemory(n-1, memory)

if __name__ == '__main__':
    # print(climbStairs(37))
    # print(climStairsRecursion(37))
    # print(climbStarsRecursionWithMemory(37, {}))
    print(climbStairsDP2(3, [1,2,3]))