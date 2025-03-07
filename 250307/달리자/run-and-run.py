n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
total = []
for i, j in zip(A, B):
    total.append(i - j)
    
cost = 0
for i in range(len(total)):
    if total[i] > 0 :
        total[i + 1] = total[i + 1] + total[i]
        cost += total[i]
print(cost)