aa = [10, 30, 15, 25, 70, 12, 15, 33, 80, 79,99, 100]
aa.append(99)  ## 추가
aa.insert(3, 77) ## 삽입 
print(aa)
#aa.remove(15) #지정한 값을 삭제
del(aa[2]) #해당 index의 값을 삭제
print(aa) 
#print(aa)
#print(aa[2])
#print(aa[0])
#print(aa[1])
#print(aa[2])
#print(len(aa))
hap = 0
for i in range(0, len(aa)) :
    hap += aa[i] 
    
print("합= %d" % hap)
print("평균=%5.2f" % (hap/len(aa)))
