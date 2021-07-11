num = int(input())
hansu = 0

for n in range(1, num+1):
    if n <= 99:
        hansu += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1
