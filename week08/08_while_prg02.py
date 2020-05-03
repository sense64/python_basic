#### 학번 이름
i, k, num =0,0,0

numStr, ch, heartStr = "","",""

### main 코드

numStr=input("숫자를 입력하세요==>")
print("") #줄바꿈

i=0
ch=numStr[i]
while True:
    num = int(ch)
    heartStr=""
    for k in range(0, num) :
        heartStr+="\u2665"

    print(heartStr)

    i+=1
    if(i > len(numStr) -1) :
        break

    ch=numStr[i]
