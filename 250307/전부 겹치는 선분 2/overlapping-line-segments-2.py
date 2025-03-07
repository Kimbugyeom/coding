n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
found = False
for i in range(n):
    for k in range(min(x1), max(x2) + 1):
        num = k
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            if x1[j] <= num <= x2[j]:
                cnt += 1
        if cnt == n - 1:
            found = True
if found:
    print('Yes')
else:
    print('No')       
        