board = [list(input()) for _ in range(10)]

# Please write your code here.
B_x = 0
B_y = 0
L_x = 0
L_y = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            B_x = i
            B_y = j
        if board[i][j] == 'L':
            L_x = i
            L_y = j

B = B_x + B_y
L = L_x + L_y
print(abs(B - L) - 1)
