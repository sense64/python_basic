# for문으로 1~10까 합을 계산하는 프로그램
hap = 0;
for i in range(1, 11) :
    hap += i
print("1~%d까지 합 = %d"%(i, hap))

#### while문 이용하기
i, hap=1,0
while(i <= 10) :
    hap += i
    i+=1

print("1~%d까지 합 = %d"%(i-1, hap))
