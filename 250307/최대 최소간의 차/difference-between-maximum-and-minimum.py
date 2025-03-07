n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
min_cost = sys.maxsize

for i in range(min(arr), max(arr) + 1):
    min_num, max_num = i, i + k
    cost = 0
    for j in range(len(arr)):
        if min_num <= arr[j] <= max_num:
            continue
        elif arr[j] > max_num:
            cost += arr[j] - max_num
        elif arr[j] < min_num:
            cost += min_num - arr[j]
    min_cost = min(min_cost, cost)

print(min_cost)

