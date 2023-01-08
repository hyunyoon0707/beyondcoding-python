import random
import time
import os
def clear():
    os.system('cls')
s = 0
for i in range(1, 6):
    z = random.randrange(1, 20)
    s += z
    print(z)
    time.sleep(2)
    clear()

while True:
    x = int(input('입력 : '))
    if x == s:
        print("정답")
        break
    else:
        continue
    
    
    






    



