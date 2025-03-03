N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts.sort(key = lambda x: (x[0] + x[1]))
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
# Please write your code here.
max_num = 0

for i in range(N):
    cost = P[i] // 2 + S[i]
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if cost + (P[j] + S[j]) > B:
            break
        cost += (P[j] + S[j])
        cnt += 1
    max_num = max(max_num, cnt)

print(max_num)

