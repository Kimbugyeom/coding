n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys

max_num = 100
min_ans = sys.maxsize

for i in range(2, max_num + 1, 2):
    for j in range(2, max_num + 1, 2):
        total_list = [0] * 4
        cnt = 0
        for x,y in points:
            if x < i and y < j:
                total_list[0] += 1
            elif x < i and y > j:
                total_list[1] += 1
            elif x > i and y < j:
                total_list[2] += 1
            elif x > i and y > j:
                total_list[3] += 1

        my_num = max(total_list)
        min_ans = min(my_num, min_ans)

print(min_ans)
                