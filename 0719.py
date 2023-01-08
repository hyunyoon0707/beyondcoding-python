# a,b = map(int,input().split())
# t = int(input())
# if b + t < 60:
#     print(a,b+t)
# elif b + t > 60:
#     k = (b+t) // 60
#     if a + k >= 24:
#         print((a+k)-24,(b+t)-60*k)
#     else:
#         print(a+k,(b+t)-60*k)
# else:
#     if a + 1 >= 24:
#         print((a+1)-24,0)
#     else:
#         print(a+1,0)


# a,b,c = map(int,input().split())
# t = int(input())
# if c+t < 60:
#     print(a,b,c+t)
# elif c + t > 60:
#     s = (c+t)//60
#     if b + s >= 60:
#         k = (b+s)//60
#         if a + k >= 24:
#             print((a+k)-24,(b+s)-60*k,(c+t)-60*s)
#         else:
#             print(a+k,(b+s)-60*k,(c+t)-60*s)
#     else:
#         print(a,b+s,(c+t)-60*s)
# else:
#     if b + 1 >= 60:
#         k = (b+1)//60
#         if a + k >= 24:
#             print((a+k)-24,(b+1)-60*k,0)
#         else:
#             print(a+k,(b+1)-60*k,0)
#     else:
#         print(a,b+1,0)                      <----- 왜 틀리는지 모르겠음 (백준 - 2530)









