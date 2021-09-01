num = int(input())
list = []

for _ in range(num):
    age, name = map(str, input().split())
    age = int(age)
    list.append((age, name))

list.sort(key=lambda member: (member[0]))

for member in list:
    print(member[0], member[1])
