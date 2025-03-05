N = int(input())
str = input()

# Please write your code here.
cnt = 1
for j in range(1, N):
    total_list = []
    for i in range(N):
        elem = str[i : i + j]

        if elem in total_list:
            found = True
            cnt += 1
            break

        total_list.append(elem)

print(cnt)