T, a, b = map(int, input().split())
c = []
x = []
list_S = []
list_N = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))
    if char == 'S':
        list_S.append(int(pos))
    elif char == 'N':
        list_N.append(int(pos))

# Please write your code here.
cnt = 0

for elem in range(a, b + 1):
    dist_S = 1000
    dist_N = 1000
    for j in range(len(list_S)):
        my_dist_s = abs(list_S[j] - elem)
        dist_S = min(my_dist_s, dist_S)

    for j in range(len(list_N)):
        my_dist_n = abs(list_N[j] - elem)
        dist_N = min(my_dist_n, dist_N)
    
    if dist_S <= dist_N:
        cnt += 1

print(cnt)
