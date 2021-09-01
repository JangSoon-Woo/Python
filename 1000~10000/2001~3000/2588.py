# 곱셈
a = int(input())
b = int(input())

o1 = a*((b % 100) % 10)
o2 = a*((b % 100)//10)
o3 = a*(b//100)
res = a*b

print(o1, o2, o3, res, sep='\n')
