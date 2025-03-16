n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0

import sys

last_idx = -sys.maxsize

for i in range(n):
    if arr[i] == 1 and i > last_idx:
        cnt += 1
        last_idx =  i + 2 * m

print(cnt)