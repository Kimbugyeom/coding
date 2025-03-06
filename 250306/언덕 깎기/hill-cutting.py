N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.
a = list(set(heights))
a.sort()
min_cost = 10000

for elem in a:
    min_elem, max_elem = elem, elem + 17
    cost = 0
    for h_elem in heights:
        if min_elem <= h_elem <= max_elem:
            continue
        elif h_elem < min_elem:
            my_cost = min_elem - h_elem
            cost += (my_cost ** 2)
        elif h_elem > max_elem:
            my_cost = h_elem - max_elem
            cost += (my_cost ** 2)
    
    if cost < min_cost:
        min_cost = cost

print(min_cost)