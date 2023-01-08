# recursive function        재귀함수

# def hello():
#     print('hello')
#     hello()

# hello()


# def factorial(n):
#     if (n == 1):
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(3))



# lambda - 한 줄 함수

# a = list(map(lambda x:int(x)+5,input().split()))

# print(a)


# zip 함수로 바꾸어 쓸 수 있음 

# def solution(mylist):
#     x = sum(mylist,[])
#     ss = []
#     s = len(mylist)
#     print(x)
#     print(s)
#     for i in range(len(mylist)):
#         k = []
#         l = i
#         while l < len(x):
#             k.append(x[l])
#             l += s
#         ss.append(k)
#     return ss

# print(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))   # 이렇게 긴 코드를 바꾸어 쓸 수 있음

# ex)   mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # new_list = [[], [], []]

        # for i in range(len(mylist)):
        #     for j in range(len(mylist[i])):
        #         new_list[i].append(mylist[j][i])     <----  이것은 그냥 위에 코드 줄인거

# ex)   mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#         new_list = list(map(list, zip(*mylist)))     <------ 이것이 zip 함수 이용해서 줄인거



# mylist = [1, 2, 3]
# new_list = [40, 50, 60]
# for i in zip(mylist, new_list):
#     print (i)

# (1, 40)
# (2, 50)
# (3, 60)        <-----  zip 함수의 사용 예            zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다. 
#                                                     튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.



# list1 = [1, 2, 3, 4]
# list2 = [100, 120, 30, 300]
# list3 = [392, 2, 33, 1]
# answer = []
# for number1, number2, number3 in zip(list1, list2, list3):
#    print(number1 + number2 + number3)                      <-----  여러 개의 Iterable 동시에 순회할 때 사용 (zip 함수 사용 예)


# animals = ['cat', 'dog', 'lion']
# sounds = ['meow', 'woof', 'roar']
# answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}   <---- Key 리스트와 Value 리스트로 딕셔너리 생성하기 (zip 함수 사용 예)
# 파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.





    
        
    






