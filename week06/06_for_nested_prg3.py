for i in range(9, 1, -1) :
    print("## %d단 ##" % i, end="  ")
print()
for i in range(9, 1, -1) :
    for j in range(9, 1, -1) :
        print("%d X %d = %d"% (j, i, i*j), end=" ")
    print()
