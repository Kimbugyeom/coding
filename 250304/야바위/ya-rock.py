n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
max_score = -1

for i in range(1, 4):
    doll = [0] * 4
    doll[i] = 1
    score = 0
    for j in range(n):
        a1, b1, c1 = a[j], b[j], c[j]
        doll[a1], doll[b1] = doll[b1], doll[a1]
        if doll[c1] == 1:
            score += 1
    max_score = max(max_score, score) 

print(max_score)