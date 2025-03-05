n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
max_count = 0
for i in range(1, n + 1):
    N = arr[i]
    total_count = 0
    for j in range(m):
        total_count += N
        N = arr[N]

    max_count = max(total_count, max_count)

print(max_count)

