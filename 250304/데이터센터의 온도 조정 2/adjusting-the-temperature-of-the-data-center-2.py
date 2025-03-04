N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

def get_score(num, ta, tb, C, G, H):
    if num < ta:
        return C
    elif ta <= num <= tb:
        return G
    else:
        return H

max_score = 0
using_num = 0
max_num = 0
for i in range(N):
    my_num = ranges[i][1]
    using_num = max(max_num, my_num)

for i in range(using_num):
    num = i
    total_score = 0
    for k in range(N):
        ta, tb = ranges[k][0], ranges[k][1]
        score = get_score(num, ta, tb, C, G, H)
        total_score += score

    max_score = max(max_score, total_score)

print(max_score)


