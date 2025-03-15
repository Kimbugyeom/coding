n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys

max_num = -sys.maxsize
plus = []
minus = []
zero = []
for i in range(n):
    if arr[i] > 0:
        plus.append(arr[i])
    elif arr[i] < 0:
        minus.append(arr[i])
    else:
        zero.append(arr[i])
plus.sort(reverse = True)
minus.sort()

#  + + +
max_plus = plus[0] * plus[1] * plus[2]
# - - +
max_minus = plus[0] * minus[0] * minus[1]

if len(plus) >= 3:
    max_plus = plus[0] * plus[1] * plus[2]
    if len(minus) >= 2:
        max_minus = plus[0] * minus[0] * minus[1]
    else:
        max_minus = 0
    max_num = max(max_plus, max_minus)
elif len(minus) >= 2:
       max_plus = 0
       max_minus = plus[0] * minus[0] * minus[1]
       max_num = max(max_plus, max_minus)
else:
    max_num = 0

print(max_num)