n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

for i in range(1, 100000):
    x = 2*i

    for j in range(n):
        found = True
        if not a[j] <= x <= b[j]:
            found = False
        else:
            x *= 2
    if found:
        print(i)
        break