n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
def get_max(i1, i2, i3):
    count = [0] * (100 + 1)
    for i in range(n):
        if i in [i1, i2, i3]:
            continue
        x1, x2 = l[i], r[i]
        for j in range(x1, x2 + 1):
            count[j] += 1
    return count

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if max(get_max(i, j, k)) < 2:
                cnt += 1

print(cnt)
            