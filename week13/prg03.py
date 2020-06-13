
def sum(v1, v2) : #sum함수를 정의
    result =0
    for i in range(v1, v2+1) :
        result += i
    return result #값을 반환

hap = sum(10, 50) #sum함수를 호출
print("합=%d" % hap)