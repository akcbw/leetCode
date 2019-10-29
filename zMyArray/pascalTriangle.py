"""

f(n,m) = f(n-1,m) + f(n-1,m-1)

"""

def triangles():
    n = 1
    previous = []
    while True:
        i = 0
        output = []
        while i < n:
            if i == 0:
                output.insert(i,1)
            elif i == n - 1:
                output.insert(i,1)
            else:
                val = previous[i] + previous[i-1]
                output.insert(i, val)
            i = i + 1
        previous = output #Remember last state
        n = n + 1
        yield output

m = 0
results = []
for t in triangles():
    results.append(t)
    m = m + 1
    if m == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')