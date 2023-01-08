a = set([1,2,3])
b = set([2,3,4])

# set
# 중복이 없다
#정해진 순서가 없다
#no index

s = set([1,2,3])
t = set('abc')

t.add('d')
t.update('efg')
t.update([1,2,3])
t.remove('a')
print(t)

print(a&b) # 교집합  = print(a.intersection(b))
print(a|b) # 합집합 = print(a.union(b))
print(a - b) # 차집합 = print(a.difference(b))



#a()() = a()의 결과가 함수일 때

def functionMaker(s):
    
    # closure = x
    
    x = s
    def printBlahBlah(a,b):
        print(a,b,x)
    
    return printBlahBlah

stringMaker = functionMaker('hello')
stringMaker('python','closure')

# for z in range(1):
#     for i in range(10):
#         x = 0
#     x+=1

# print(x+1)

# def s():
#     global x
#     x = 1
# s()
# print(x+1)





