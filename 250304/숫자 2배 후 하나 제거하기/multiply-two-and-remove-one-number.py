n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
min_total = sys.maxsize

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        total = []
        for k in range(n):
            if j != k:
                total.append(arr[k])
        my_total = 0
        for w in range(len(total) - 1):
            my_total += abs(total[w] - total[w + 1])
        
        min_total = min(min_total, my_total)

    arr[i] //= 2

print(min_total)

