n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
max_cnt = -1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        x1, x2 = i, j
        cnt = 0
        for k in range(m):
            if (x1 == pairs[k][0] and x2 == pairs[k][1]) or (x1 == pairs[k][1] and x2 == pairs[k][0]):
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)