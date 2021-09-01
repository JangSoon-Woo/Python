# X보다 작은수
a, b = map(int, input().split())
c = list(map(int, input().split()))
for i in c:
    if i < b:
        print(i, end=" ")
