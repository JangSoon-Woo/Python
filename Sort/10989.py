N = int(input())

check_list = [0] * 10000
for i in range(N):
    input_num = int(input())
    check_list[input_num - 1] = check_list[input_num - 1] + 1

for i in range(10000):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i+1)
