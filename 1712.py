# 총 수입(판매비용)이 총 비용(=고정비용+가변비용)
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(int(A/(C-B))+1)
