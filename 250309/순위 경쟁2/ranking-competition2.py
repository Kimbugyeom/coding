n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
count = [0, 0]
winner = [('A','B')]
cnt = 0

for i, j in zip(c, s):
    if i == 'A':
        count[0] += j
    else:
        count[1] += j
    
    if count[0] < count[1]:
        winner.append('B')
    elif count[0] > count[1]:
        winner.append('A')
    else:
        winner.append(('A','B'))

for i in range(len(winner) - 1):
    if winner[i] != winner[i + 1]:
        cnt += 1

print(cnt)