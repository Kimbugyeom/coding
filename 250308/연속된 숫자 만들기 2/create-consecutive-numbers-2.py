pos = list(map(int, input().split()))

# Please write your code here.
x1, x2, x3 = pos[0], pos[1], pos[2]

if x2 - 2 <= x1 <= x2 + 2 or x2 - 2 <= x3 <= x2 + 2:
    print(1)
else:
    print(2)