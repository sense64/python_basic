# for문을 이용하여 피보나치 수열값을 구함(수열값이 100이 넘어가면 중단
num1, num2, num3 = 1, 1, 0;
print(num1, " ", num2, end= " ")
for i in range(1,51) :
    num3 = num1 + num2
    print(num3, end=" ")
    if num3 > 100 :
        break
    num1 = num2
    num2 = num3
