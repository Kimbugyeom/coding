n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys

min_ans = sys.maxsize

for i in range(n):
    min_x = 100
    min_y = 0
    for j in range(n):
        if i == j:
            continue
        min_x = min(min_x, segments[j][0])
        min_y = max(min_y, segments[j][1])

    ans = abs(min_y - min_x)
    
    min_ans = min(min_ans, ans)

print(min_ans)