n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
new_blocks = blocks.copy()
need_blocks = sum(blocks) // n
cnt = 0
for i in range(n):
    new_blocks[i] = new_blocks[i] - need_blocks
    if new_blocks[i] < 0:
        cnt += abs(new_blocks[i])

print(cnt)