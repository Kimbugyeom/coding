a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if b < c or d < a:
    print((b - a) + (d - c))
elif a <= c <= b <= d:
    print(d - a)
elif c <= a <= d <= b:
    print(b - c)
else:
    print(max(a,b,c,d) - min(a,b,c,d))
