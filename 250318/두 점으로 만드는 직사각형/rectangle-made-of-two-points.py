x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
new_x1 = min(x1, a1)
new_y1 = min(y1, b1)
new_a1 = max(x2, a2)
new_b1 = max(y2, b2)

x = abs(new_a1 - new_x1)
y = abs(new_b1 - new_y1)
print(x * y)