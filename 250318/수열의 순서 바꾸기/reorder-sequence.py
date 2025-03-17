n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
idx = n - 2
while idx >= 0 and sequence[idx] < sequence[idx + 1]:
    idx -= 1

print(idx + 1)
    