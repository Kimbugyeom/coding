N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
import sys

max_num = -sys.maxsize

for i in range(len(num)):
    dist = 0
    found = False
    fire_num = 0
    for j in range(len(num)):
        if i == j:
            continue

        if num[i] == num[j]:
            dist = abs(i - j)

        if 0 < dist <= K:
            found = True
            fire_num = num[i]
    
    if found:
        max_num = max(max_num, fire_num)

if max_num > 0:
    print(max_num)
else:
    print(-1)
