board = [list(input()) for _ in range(10)]

# Please write your code here.
B_x = 0
B_y = 0
L_x = 0
L_y = 0
R_x = 0
R_y = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            B_x = i
            B_y = j
        if board[i][j] == 'L':
            L_x = i
            L_y = j
        if board[i][j] == 'R':
            R_x = i
            R_y = j

x = abs(B_x - L_x)
y = abs(B_y - L_y)

if B_x == R_x == L_x or L_y == B_y == R_y:
    if (R_x < B_x and R_x < L_x) or (B_x < R_x and B_x < R_x) or (R_y < B_y and R_y < L_y) or (B_y < R_y and B_y < R_y):
        print(x + y - 1)
    else:
        print(x + y + 1)
else:
    print(x + y - 1)
