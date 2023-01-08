# x = input()
# s = 10
# for i in range(1,len(x)):
#     if x[i] == x[i-1]:
#         s += 5
#     else:
#         s += 10
# print(s)


# x = int(input())
# for i in range(x,0,-1):
#     print(' '*(x-i)+'*'*i)


# x = int(input())
# for i in range(x,0,-1):
#     print(' '*(x-i)+'*'*(2*i-1))



# x = int(input())
# if x == 1:
#     print(1%10007)
# elif x == 2:
#     print(2%10007)
# else:
#     s = [1,2]
    
#     for i in range(x-2):
#         k = s[i] + s[i+1]
#         s.append(k)
#     print(max(s)%10007)


# x = int(input())
# for i in range(x,0,-1):
#     print(' '*(x-i)+'*'*(2*i-1))
# for i in range(2,x+1):
#     print(' '*(x-i)+'*'*(2*i-1))


# x = int(input())
# if x == 1:
#     print(1%10007)
# elif x == 2:
#     print(3%10007)
# else:
#     s = [1,3]
    
#     for i in range(x-2):
#         k = s[i] + s[i+1] + s[i]
#         s.append(k)
#     print(max(s)%10007)



# x = int(input())
# if x == 1:
#     print(1)
# elif x == 2:
#     print(3)
# else:
#     s = [1,3]
        
#     for i in range(x-2):
#         k = s[i] + s[i+1] + s[i]
#         s.append(k)
#     print(max(s))


# s = []
# while True:
#     x = input()
#     if x == '=':
#         break
#     s.append(x)

# for i in s:
#     t = 0
#     if i == '+':
#         t += (int(s[s.index(i)-1]) + int(s[s.index(i)+1]))
#         s.remove(s[s.index(i)-1:s.index(i)+2])
#         # s(s[s.index(i)-1])
#         # s.remove(s[s.index(i)+1])
#         # s.remove(i)
#         s.insert(0,t)
#     elif i == '-':
#         t += (int(s[s.index(i)-1]) - int(s[s.index(i)+1]))
#         s.remove(s[s.index(i)-1:s.index(i)+2])
#         s.insert(0,t)
#     elif i == '*':
#         t += (int(s[s.index(i)-1]) * int(s[s.index(i)+1]))
#         s.remove(s[s.index(i)-1:s.index(i)+2])
#         s.insert(0,t)
#     else:
#         t += (int(s[s.index(i)-1]) // int(s[s.index(i)+1]))
#         s.remove(s[s.index(i)-1:s.index(i)+2])
#         s.insert(0,t)
# print(max(s))



import cv2 as cv
from PIL import Image
# img = cv.imread('cat.jpeg')
# cv.imshow("Cat",img)

def resize(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv.resize(frame,(width,height))

video = cv.VideoCapture(0)  # 'dog.mp4'  
ascii_chars = """&@WM%8D#b$0NqGXOEyVS2xCj}t?lv^i/r7<+!*~";_:,'-.`"""

def image_to_ascii(image):
    pixels = image.getdata()

    characters = []
    for pixel in pixels:
        characters.append(ascii_chars[pixel//int(255//len(ascii_chars)+1)])   
    characters = ''.join(characters)
    
    pixel_count = len(characters)
    ascii_image = []
    for i in range(0,pixel_count,200):
        ascii_image.append(characters[i:i+200])
    ascii_image = '\n'.join(ascii_image)

    print(ascii_image)
    # with open("ascii.txt",'w') as f:
    #     f.write(ascii_image)
while True:
    isTrue,frame = video.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    ratio = frame.shape[1]/frame.shape[0]
    
    small_img = cv.resize(gray, (200,int(ratio*200)), interpolation=cv.INTER_AREA)
    image_to_ascii(Image.fromarray(small_img))
    
    cv.imshow("video",frame)
    
    resized_frame = resize(frame,0.5)
    cv.imshow('small video',resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()

cv.waitKey(0)
















        
    
        

        
   
    


    

    
    



