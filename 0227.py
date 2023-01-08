# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = 0
# x = int(input())
# for i in a:
#     if i == x:
#         s += 1
# print(s)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# x = int(input())
# for i in range(len(a)):
#     if x not in a:
#         print("no")
#         break
#     elif a[i] == x:
#         print(i)
#         break

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = []
# for i in a:
#     if i < 5:
#         s.append(i)
# print(s)



#replace (문자 변형)
# s = 'hello world'
# print(s.replace('world', 'python'))

#split (문자 쪼개기)
# s = 'hello world'
# s = s.split()
# print(s)

#s = 'hello - world'
#s = s.split('-')
#print(s)

#join (문자 합치기)
#s = 'hello world'
#s = s.split() (문자 쪼개기)
#s = ' '.join(s)
#print(s)

#upper (대문자)
#s = 'hello'
#print(s.upper())

#lower (소문자)
#print(s.lower())


#strip (공백 제거)
#s = '    hello     '
#print(s.strip())




# s = 'a b c d e f'
# s = s.split()
# s = '*'.join(s)
# print(s)

# s = "5,000,000,000"
# print(s.replace(',', ''))


# x = input()
# for i in x:
#     if i == 'o':
#         print(i)

# x = input()
# for i in x:
#     if i == 'o':
#         x = x.replace('o', 'x')
# print(x)

# x = input()
# s = []
# for i in x:
#     if i == 'o':
#         s.append(i)
# print(''.join(s))

# x = input()
# s = 0
# for i in x:
#     if i == 'o':
#         s += 1
#     elif i == 'x':
#         s -= 1
# print(s)

# x = input()
# s = 0
# for i in range(len(x)):
#     if x[i] == 'o':
#         for z in range(-1,len(x) -1):
#             s = s + (2 * (z+2) - (z+2))
            
#             if x[(i+1)] == 'x':
#                 break
    
#     elif x[i] == 'x':
#         for y in range(-1,len(x) -1):
#             s = s - (2 * (y+2) - (y+2))
#             if x[(i+1)] == 'o':
#                 break
# print(s)


# x = input()
# s = 0
# for i in range(0, len(x) - 1):
#     if x[i] == 'o':
#         for z           
            
        
    
#     elif x[i] == 'x':
#         for y in range(-1,len(x) -1):
#             if x[y+2] == 'o':
#                 s -= 1
#                 break
        
#         s = s - (2 * (y+2) - (y+2))
            
            
       
# print(s)

#dict (dictionary)
#a = {"hello":100, "hi":"bye", "python":["java", "c"]}
#print(a["a"])
#print(a["hi"])
#a = {"a":100, "b":1000}
#값 바꾸기
#a["a"] = 0 아니면 a.update(a = 10)
#print(a["a"])

#길이
#print(len(a))
#추가하기
#a.update(c = 1000)
#삭제하기
#a.pop("a")
#클리어
#a.clear()
#print(a)
#키값
#print(a.keys())
#값들
#print(a.values())
#전체
#print(a.items())
#키값, 값들, 전체 = for문과 같이 사용
#전체 = for i, j = a.items(): 과 같이 사용(두개로 받아줌) 
#print(i, j)

# x = {"a":100, "b":200, "c":23, "d":38924, "e":31}
# s = 0
# for i in x.values():
#     s += i
# print(s)

# x = {"a":100, "b":200, "c":23, "d":38924, "e":31}
# x.update({"b":300})
# x.pop("c")
# print(x)

# inventory = {"메로나":[300, 20],
#             "비비빅":[400, 3],
#             "죠스바":[250, 100]}
# inventory.update(월드콘 = [500, 7]) 
# inventory["메로나"][0] = 10
# print(inventory)





         
    
    



























