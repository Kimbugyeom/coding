pos = list(map(int, input().split()))

# Please write your code here.
x1, x2, x3 = pos[0], pos[1], pos[2]


if x1 + 1 == x2 and x2 + 1 == x3:
    print(0)
elif x3 + 1 == x2 and x2 + 1 == x1:
    print(0)
else:
    print(2)