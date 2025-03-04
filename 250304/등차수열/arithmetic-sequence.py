n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_a = max(a)

cnt = 0
for N in range(1, max(a)):
    for j in range(len(a)):
        if abs(a[j] - N) == abs(a[j - 1] - N):
            cnt += 1

print(cnt)