from math import gcd


def LCM(a, b):
    d = gcd
    return int((a * b) / d)


def GCD(a, b):
    return gcd(b % a, a) if a % b else a


T = int(input())
for i in range(t):

    a, b = map(int, input().split())
    print(LCM(a, b))

# 런타임 에러
