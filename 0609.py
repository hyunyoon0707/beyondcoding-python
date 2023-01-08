s=[]
while True:
    x = int(input())
    if x == -1:
        break
    s.append(x)

for i in s:
    ss = []
    c = 0
    for z in range(1,i):
        if i % z == 0:
            ss.append(str(z))
            ss.append('+')
    
    for k in range(0,len(ss),2):
        c += int(ss[k])
    if c == i:
        
        ss.pop()
        print(f"{i} = {' '.join(ss)}")
    else:
        print(f"{i} is Not perfect")





        
        



    





