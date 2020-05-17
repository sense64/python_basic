#변수 선언
aa=[]  #리스트 자료구조 선언
hap=0
avg = 0.0
v = 0.0
for i in range(0, 5) :
    aa.append(int(input(str(i+1) + "번째 숫자를 입력==>")))

#hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] 반복문으로 수정

for i in range(0, len(aa)) :
    hap += aa[i]
    
avg = hap / len(aa)

for i in range(0, len(aa)) : #분산을 계산
    v+=(aa[i] - avg) ** 2
    
print("합=%d, 평균=%6.2f, 분산=%6.2f" % (hap, avg, v/len(aa)))


