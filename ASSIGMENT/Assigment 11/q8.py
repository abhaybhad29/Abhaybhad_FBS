#Print 1 to 100 in snakes and ladder pattern.
for i in range(10, 0, -1):
    if i % 2 == 0:
        for j in range((i-1)*10+1, i*10+1):
            print(j, end=" ")
    else:
        for j in range(i*10, (i-1)*10, -1):
            print(j, end=" ")
    print()