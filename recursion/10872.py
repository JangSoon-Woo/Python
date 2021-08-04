n = int(input())

R = 1
if n > 0:
    for i in range(1, n+1):
        R *= i
print(R)