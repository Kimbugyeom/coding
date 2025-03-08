pos = list(map(int, input().split()))

# Please write your code here.
x1, x2, x3 = pos[0], pos[1], pos[2]

675
if x1 + 1 == x2 and x2 + 1 == x3:
    print(0)
elif x3 + 1 == x2 and x2 + 1 == x1:
    print(0)
elif x3 + 1 == x1 and x1 + 1 == x2:
    print(0)
elif x2 + 1 == x1 and x1 + 1 == x3:
    print(0)
elif x1 + 1 == x3 and x3 + 1 == x2:
    print(0)
elif x2 + 1 == x3 and x3 + 1 == x1:
    print(0)
elif x2 - 1 <= x1 <= x2 + 1 or x2 - 1 <= x3 <= x2 + 1:
    print(2)
elif x2 - 2 <= x1 <= x2 + 2 or x2 - 2 <= x3 <= x2 + 2:
    print(1)
else:
    print(2)