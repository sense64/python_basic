#### 학번 이름  ####
i, k =5, 0

while i < 9 :
    k=0
    while k < i-4 :
        print("  ", end="")
        k+=1
    k=0
    while k < (9-i) *2 -1 :
        print("\u2605", end="")
        k+=1
        
    print()
    i += 1
    
