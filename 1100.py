chess = []
for _ in range(8):
    chess.append(list(map(str, list(input()))))

aw = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            
print(aw)
# 미완