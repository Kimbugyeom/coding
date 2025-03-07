n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
found = False
for i in range(min(x1), max(x2) + 1):
    num = i
    cnt = 0
    for j in range(n):
        if x1[j] <= num <= x2[j]:
            cnt += 1
    
    if cnt == n:
        found = True

if found:
    print('Yes')
else:
    print('No')
    