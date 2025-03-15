n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a)  # 리스트 정렬
min_num = a_sorted[0]  # 가장 작은 값
second_num = -1  # 2번째로 작은 값 초기화

# 2번째로 작은 값 찾기
for num in a_sorted:
    if num > min_num:
        second_num = num
        break

if second_num == -1:
    print(-1)
    exit()

second_idx = -1
count = 0
for i in range(n):
    if a[i] == second_num:
        count += 1
        if count == 1:
            second_idx = i + 1

if count == 1:
    print(second_idx)
else:
    print(-1)
