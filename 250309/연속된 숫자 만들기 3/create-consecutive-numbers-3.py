a = list(map(int, input().split()))

# Please write your code here.
x1, x2, x3 = a[0], a[1], a[2]
max_num1 = x2 - x1 - 1
max_num2 = x3 - x2 - 1

if x1 + 1 == x2 and x2 + 1 == x3:
    print(0)
else:
    ans = max(max_num1, max_num2)
    print(ans)