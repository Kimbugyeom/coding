X, Y = map(int, input().split())

# Please write your code here.
cnt = 0
for elem in range(X, Y + 1):
    n = elem
    my_list = []
    while n > 0:
        my_list.append(n % 10)

        n //= 10

    if my_list == my_list[::-1]:
        cnt += 1
print(cnt)