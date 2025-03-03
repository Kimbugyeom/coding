k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
total = []

for i in range(k):
    use_arr = arr[i]
    for j in range(n):
        for w in range(j + 1, n):
            x1, x2 = use_arr[j], use_arr[w]
            total.append((x1, x2))

final = []
total_cnt = 0
for i in range(len(total)):
    target_x, target_y = total[i][0], total[i][1]
    cnt = 1
    for j in range(len(total)):
        if i == j:
            continue
        x, y = total[j][0], total[j][1]
        if x == target_x and y == target_y:
            cnt += 1
    if cnt == k:
        total_cnt += 1

print(total_cnt // k)
            