X = int(input())

# Please write your code here.
speed = 1
dist = 1
time = 1
cnt = 0
while dist < X:
    if dist <= X // 2:
        speed += 1
        dist += speed
        time += 1

    elif dist > X // 2:
        if speed > 1:
            speed -= 1
        else:
            speed = 1
            cnt += 1
        dist += speed
        time += 1

if speed > 1 :
    print(time + speed - 1)
elif speed == 1 and cnt > 1:
    print(time - cnt + 1)
else:
    print(time)