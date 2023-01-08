# x = list(map(int,input().split()))
# y = x.copy()
# for i in range(len(x)):
#     x[i],x[x.index(min(y))] = x[x.index(min(y))],x[i]
#     y.remove(min(y))
# print(*x)

# x = list(map(int,input().split()))
# for i in range(len(x)):
#     a = x.index(min(x[i:]))
#     x[i],x[a] = x[a],x[i]
# print(x)

# while True:
#     x = input()
#     t = 0
#     for i in range(len(x)):
#         if x[i] == x[len(x)-i-1]:
#             t += 1
#     print(t)
#     if len(x) % 2 == 0 and t % 2 == 0:
#         print("yes")
#     elif len(x) % 2 == 0 and t % 2 != 0:
#         print("no")
#     elif len(x) % 2 != 0 and (t-1) % 2 == 0:
#         print("yes")
#     else:
#         print("no")
        






# x = list(map(int,input().split()))
# # y = x.copy()
# for i in range(1,len(x)):
    
#     for z in range(i,0,-1):
        
#         # if x[x.index(y[i])] < x[z]:
            
#         #     x[x.index(y[i])],x[z] = x[z],x[x.index(y[i])]
            
#         if x[z] < x[z-1]:
#             x[z-1], x[z] = x[z], x[z-1]
#             print(x)
#         else:
#             continue

# print(x)   


import cv2 as cv

# img = cv.imread('cat.jpeg')
# cv.imshow("Cat",img)

def resize(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv.resize(frame,(width,height))

video = cv.VideoCapture(0)  # 'dog.mp4'  
while True:
    isTrue,frame = video.read()
    cv.imshow("video",frame)
    
    resized_frame = resize(frame,0.5)
    cv.imshow('small video',resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()

cv.waitKey(0)






