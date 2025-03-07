N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
my_list = []
for elem in b:
    dist = elem
    cnt = 0
    using_L = L
    for i in range(len(a)):
        if a[i] >= dist:
            cnt += 1
        else:
            if using_L >= 1:
                if a[i] + 1 >= dist:
                    cnt += 1
                    using_L -= 1

    if cnt >= dist:
        my_list.append(dist)

print(max(my_list))
    