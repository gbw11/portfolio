money = int(input())


cnt = 0
while money:
    if money>=500:
        money -= 500
        cnt +=1

    elif money>=100:
        money -= 100
        cnt +=1

    elif money>=50:
        money -= 50
        cnt +=1

    elif money>= 10:
        money -= 10
        cnt +=1

print(cnt)