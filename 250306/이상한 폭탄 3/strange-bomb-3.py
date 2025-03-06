N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
max_cnt = 0
max_idx = 0

for elem in range(1, 1000001):
    x = elem
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if num[i] == elem and num[j] == elem and abs(i - j) <= K:
                cnt += 1

    if max_cnt <= cnt:
        max_cnt = cnt
        max_idx = x

if max_idx == 1000000:
    print(0)
else:
    print(max_idx) 