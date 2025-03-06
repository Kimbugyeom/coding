N = int(input())
seat = list(input())

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = '1'
            seat[j] = '1'

            min_dist = N 
            for k in range(N - 1):
                for w in range(k + 1, N):
                    if seat[k] == '1' and seat[w] == '1':
                        dist = abs(w - k)
                        min_dist = min(min_dist, dist)
            ans = max(ans, min_dist)

            seat[i] = '0'
            seat[j] = '0'

print(ans)