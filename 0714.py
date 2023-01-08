# a = 7
# b = 3
# print(*divmod(a,b))
# a = 7
# b = 3
# print(divmod(a,b))

# print(type(divmod))


# *divmod(a,b) = a를 b로 나눈 몫과 나머지를 알고 싶을 때 사용







# a,b = input().split()                                              a,b = input().split()
# s = [int(i) for i in a]                                            s = 0
# k = 0                                                              for i, j in enumerate(a[::-1]):
# for i in range(1,len(s)+1):                                           s += int(j) * (int(b)**i) 
                                                                    #print(s)
#     k += s[i-1] * (int(b)**(len(s)-i))     --->       더 쉽게 쓰면 
    
# print(k)
    

# ------> 더 쉽게 쓰면  
# a,b = input().split()
# answer = int(a,int(b))      # 'a' must be str and 'b' must be int
# print(answer)




### 우측 정렬 예
s = input()
n = 7

print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

s,n = input().split()
n = int(n)

answer = ''
if n % 2 == 0:
    for i in range(((n//2)+(n//2+1)/2)):
        answer += ' '
    answer += s
else:
    for i in range(n-(n//2+1)): 
        answer += ' '
    answer += s
print(s)
print(answer)
print(' '*(n-2)+s)





# string 에서 불러오기

import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789





# sorted 함수로 정렬된 새로운 리스트 만들기 //  copy 와 sort 함수를 이용하여도 만들 수 있지만 이 경우 복제한 리스트와 원래 리스트가 같이 정렬된다.
list1 = [3, 2, 5, 1]
list2 = sorted(list1)



