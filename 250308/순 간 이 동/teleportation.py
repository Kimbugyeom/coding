a, b, x, y = map(int, input().split())

# Please write your code here.
dist = []

case1 = abs(b - a)
dist.append(case1)

case2 = abs(a - x) + abs(b- y)
dist.append(case2)

case3 = abs(a - y) + abs(b - x)
dist.append(case3)

print(min(dist))