A, B, C = map(int, input().split())

# Please write your code here.
import sys
min_ans = -sys.maxsize

max_num = 1000
new_A = A
for i in range(max_num):
    new_A = A * i
    new_B = B
    for j in range(max_num):
        new_B = B * j
        total = new_A + new_B
        if total > C:
            break
        min_ans = max(total, min_ans)

print(min_ans)