n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.
for j in range(1, n + 1):
    ans = [0] * n
    ans[0] = j
    for k in range(1, n):
        found = False
        ans[k] = adjacent[k - 1] - ans[k - 1]
        if ans[k] < 1 or ans[k] > n or ans[k] == ans[k - 1]:
            found = False
            break
        else:
            found = True
    if found:
        for w in ans:
            print(w, end= ' ')
        break