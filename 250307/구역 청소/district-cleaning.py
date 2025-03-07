a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if b < c or d < a:
    print((b - a) + (d - c))
elif b >= c and a > d:
    print(d - a)
elif a <= d and b >= c:
    print(b - c)
