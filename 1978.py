n = int(input())

numbers = map(int, input().split())
sosu = 0
for num in numbers:
    er = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                er += 1
        if er == 0:
            sosu += 1
print(sosu)
