case = int(input())

for _ in range(case):
    mars = list(map(str, input().split()))
    re = 0
    for i in range(len(mars)):
        if i == 0:
            re += float(mars[i])
        else:
            if mars[i] == "#":
                re -= 7
            elif mars[i] == "%":
                re += 5
            elif mars[i] == "@":
                re *= 3

    print("%0.2f" % re)
