import math

m, n = map(int, input().split())
lst = [i for i in range(m, n+1)]
lst = set(lst)


for i in range(2, int(math.sqrt(n) + 1)):
    j = 2
    while (i * j <= n):
        if i * j in lst:
            lst.remove(i * j)
        j += 1
lst = list(lst)
lst.sort()
# 미완?
