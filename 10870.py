def fi(num):
    if num<=1:
        return num
    return fi(num-1)+fi(num-2)

n=int(input())
print(fi(n))