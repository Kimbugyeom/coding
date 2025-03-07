n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.
user_list = []
for i in range(n):
    user_list.append(chr(ord('A') + i))
read_list = []

for i in range(m):
    user, num = c[i], u[i]
    if i >= p - 1:
        read_list.append(user)

for elem in user_list:
    if elem not in read_list:
        print(elem, end = ' ') 

