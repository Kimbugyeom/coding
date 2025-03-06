nums = list(map(int, input().split()))
nums.sort()
# Please write your code here.
for a in range(1, 11):
    for b in range(a, 11):
        for c in range(b, 11):
            for d in range(c, 11):
                my_list = [a, b, c, d, a + b, b + c, c + d, d + a, a + c, b + d, a + b + c, a + b+ d, a+ c+ d, b+ c+ d, a+b+c+d]
                my_list.sort()
                if my_list == nums:
                    print(a, b, c, d)
                    break

                