n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
ans_list = []

for i in range(n):
    ans = abs(arr[i] - arr[i + n])
    ans_list.append(ans)

print(min(ans_list))