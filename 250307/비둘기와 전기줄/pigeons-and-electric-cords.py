N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
new_list = []
for i,j in zip(pigeon, position):
    new_list.append((i, j))
new_list.sort(key = lambda x: x[0])

pigeon = []
position = []

for i,j in new_list:
    pigeon.append(i)
    position.append(j)

cnt = 0
for i in range(N - 1):
    if pigeon[i] != pigeon[i + 1]:
        continue
    if position[i] != position[i + 1]:
        cnt += 1  
print(cnt) 