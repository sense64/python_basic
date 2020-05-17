aa = [10, 30, 15, 25, 70]
aa.append(20)
aa.append(60)
hap = 0
for i in range(0, len(aa)) :
    hap+= aa[i]

print("합 = %d" %  hap)
print("평균 = %5.2f" % (hap/len(aa)))



