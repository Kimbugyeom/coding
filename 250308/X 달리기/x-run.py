X = int(input())

# Please write your code here.
speed = 1
dist = 1
time = 1

while dist < X:
    if dist <= X / 2:
        speed += 1
        dist += speed
        time += 1

    elif dist > X / 2:
        if speed > 1:
            speed -= 1
        else:
            speed = 1
        dist += speed
        time += 1

print(time)