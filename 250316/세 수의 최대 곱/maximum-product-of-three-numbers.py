n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_num = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] * arr[j] * arr[k] > max_num:
                max_num = arr[i] * arr[j] * arr[k]

print(max_num)