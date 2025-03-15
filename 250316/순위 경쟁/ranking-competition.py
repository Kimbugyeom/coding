n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
count = [0, 0, 0]
winner = [count]

for i, j in zip(c, s):
    if i == 'A':
        count[0] += j
    elif i == 'B':
        count[1] += j
    else:
        count[2] += j
    
    new_count = count.copy()
    max_num = max(new_count)
    for k in range(len(new_count)):
        if new_count[k] == max_num:
            new_count[k] = 1
        else:
            new_count[k] = 0

    winner.append(new_count) 

winner[0] = [0, 0, 0]

cnt = 0
for i in range(n):
    if winner[i] != winner[i + 1]:
        cnt += 1

print(cnt)