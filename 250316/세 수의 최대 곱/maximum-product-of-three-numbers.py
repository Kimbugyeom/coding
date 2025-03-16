import sys

n = int(input())
arr = list(map(int, input().split()))

max_num = -sys.maxsize
plus = []
minus = []
zero = False

for num in arr:
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero = True

plus.sort(reverse=True)
minus.sort()

candidates = []

if len(plus) >= 3:
    candidates.append(plus[0] * plus[1] * plus[2])

if len(plus) >= 1 and len(minus) >= 2:
    candidates.append(plus[0] * minus[0] * minus[1])

if len(minus) >= 3:
    candidates.append(minus[-1] * minus[-2] * minus[-3])

if len(minus) >= 2 and len(plus) == 1:
    candidates.append(plus[0] * minus[-1] * minus[-2])

if len(plus) >= 2 and len(minus) == 1:
    candidates.append(plus[-1] * plus[-2] * minus[0])

if zero:
    candidates.append(0)

print(max(candidates))

