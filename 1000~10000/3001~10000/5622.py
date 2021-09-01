di = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
re = 0

for j in range(len(a)):
    for i in di:
        if a[j] in i:
            re += di.index(i)+3
print(re)
