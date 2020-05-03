#### 학번 이름  ####
i, k =0, 0

while i < 5 :
    k=0
    while k < 4-i :
        print("  ", end="")
        k+=1
    k=0
    while k < i*2 +1 :
        print("\u2605", end="")
        k+=1
        
    print()
    i += 1
    
