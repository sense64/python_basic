#변수 선언
aa=[]
hap=0
avg, v =0.0, 0.0

for i in range(0, 5) :
    aa.append(int(input(str(i+1) + "번째 숫자를 입력==>")))

for i in range(0, len(aa)) :
    hap+=aa[i]

avg = hap / len(aa)

for i in range(0, len(aa)) :
    v += (aa[i] - avg) ** 2

print("합=%d, 평균=%f, 분사=%f"% (hap, avg, v/len(aa))) 
    
