n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_a = max(a)
min_a = min(a)

max_cnt = 0
for N in range(min_a, max_a):
    cnt = 0
    for j in range(len(a)):
        for k in range(len(a)):
            if j == k:
                continue
            if abs(a[j] - N) == abs(a[k] - N):
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(int(max_cnt/2))