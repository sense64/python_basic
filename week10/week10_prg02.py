aa=[
    [3, 50, 20],
    [90, 30, 70, 90, 10],
    [60, 20, 40, 20]
]
s=[0, 0, 0]
for i in range(0, len(aa)) :
    for j in range(0, len(aa[i])) :
        print(aa[i][j], end="  ")
        s[i] += aa[i][j]
    print()

for i in range(0, len(s)):
    print("행의 합 =%d, 평균 = %f" % (s[i], s[i]/len(aa[i])))


