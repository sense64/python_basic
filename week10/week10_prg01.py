## 리스트 초기화 ##
aa = [80, 40, 60, 70, 25]
## 리스트 선언 ##
bb = []


cc = aa
bb = list(aa)
dd = aa.copy()
dd[2] = 3000
aa[2]=1000
cc[3] =500
bb[1] = 90
print(aa)
print(bb)
print(cc)
print(dd)

