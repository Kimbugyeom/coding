N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
max_elem = 0

for a in range(10000):
    my_list = []
    for elem in arr:
        if a <= elem and elem <= a + K:
            my_list.append(elem)

    max_elem = max(max_elem, len(my_list))

print(max_elem)