X, Y = map(int, input().split())

max_num = 0

for num in range(X, Y + 1):
    cnt = 0
    temp = num 

    while temp > 0:
        cnt += temp % 10
        temp //= 10

    max_num = max(max_num, cnt)

print(max_num)
