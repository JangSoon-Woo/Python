num = int(input())
stlist = []

for _ in range(num):
    weight, height = map(int, input().split())
    stlist.append((weight, height))

for i in stlist:
    rank = 1
    for j in stlist:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
