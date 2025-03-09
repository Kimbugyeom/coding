N = int(input())
seats = list(input())

# Please write your code here.
ans = 0

for i in range(N):
    if seats[i] == '0':
        seats[i] = '1'
    
        min_dist = N
        for j in range(N - 1):
            for k in range(j + 1, N):

                if seats[j] == '1' and seats[k] == '1':
                    min_dist = min(min_dist, abs(j - k))
        ans = max(ans, min_dist)

        seats[i] = '0'

print(ans)
    
