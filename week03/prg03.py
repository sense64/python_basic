#학번 이름 원의 면적 및 둘레
r=eval(input("반지름=>")) #자료형 변환 함수 : int(), float(), eval()
PI = 3.14159 # 3.14를 PI상수로 지정
area = r*r*PI #면적
c = 2*r*PI #둘레
v = (4/3)*PI*r*r #구의 부피
print("면적 : ",area)
print("둘레 : ", c)
print("구의 부피 : %7.2f" % v)

