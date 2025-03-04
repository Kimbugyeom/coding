N = int(input())
a = [int(input()) for _ in range(N)]


max_a = max(a)

max_cnt = 0

for H in range(1, max_a):
    cnt = 0
    count = [0] * (N)
    for i in range(N):
        new = a[i] - H
        if new <= 0:
            new = 0
        else:
            new = 1
        count[i] = new
    for j in range(N):
        if count[j] == 1 and (j == 0 or count[j-1] == 0):
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
