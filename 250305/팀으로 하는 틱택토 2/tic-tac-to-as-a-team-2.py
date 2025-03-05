inp = [list(map(int, input())) for _ in range(3)]

max_num = 9
cnt = 0

for i in range(1, max_num + 1):
    for j in range(1, max_num + 1):
        if i == j:
            continue

        for k in range(3):
            if not (inp[k][0] == i and inp[k][1] == i and inp[k][2] == i) and \
               not (inp[k][0] == j and inp[k][1] == j and inp[k][2] == j) and \
               (inp[k][0] in [i, j] and inp[k][1] in [i, j] and inp[k][2] in [i, j]):
                cnt += 1

        for k in range(3):
            if not (inp[0][k] == i and inp[1][k] == i and inp[2][k] == i) and \
               not (inp[0][k] == j and inp[1][k] == j and inp[2][k] == j) and \
               (inp[0][k] in [i, j] and inp[1][k] in [i, j] and inp[2][k] in [i, j]):
                cnt += 1

        if not (inp[0][0] == i and inp[1][1] == i and inp[2][2] == i) and \
           not (inp[0][0] == j and inp[1][1] == j and inp[2][2] == j) and \
           (inp[0][0] in [i, j] and inp[1][1] in [i, j] and inp[2][2] in [i, j]):
            cnt += 1

        if not (inp[0][2] == i and inp[1][1] == i and inp[2][0] == i) and \
           not (inp[0][2] == j and inp[1][1] == j and inp[2][0] == j) and \
           (inp[0][2] in [i, j] and inp[1][1] in [i, j] and inp[2][0] in [i, j]):
            cnt += 1

print(cnt//2)
