n = int(input())
arr = list(input().split())

# Please write your code here.
total_cnt = 0
ord_arr = []
new_arr = []

for i in range(len(arr)):
    ord_arr.append(ord(arr[i]) - 65)
    new_arr.append(i) 

total_cnt = 0
for i in range(n):
    if ord_arr[i] == new_arr[i]:
        continue
    else:
        total_cnt += abs(ord_arr[i] - new_arr[i])
        new_arr[i] += abs(ord_arr[i] - new_arr[i])
        for j in range(i + 1, n):
            new_arr[j] = new_arr[j] - 1

    if new_arr == ord_arr:
        break

print(total_cnt)
