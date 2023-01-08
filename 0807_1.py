import cv2 as cv
from PIL import Image

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

    with open("ascii.txt",'w') as f:
        f.write(ascii_image)
    
img = cv.imread("cat.jpeg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# brul =  cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)

# canny = cv.Canny(img, 100,100)

# small_img = cv.resize(gray, (200,150), interpolation=cv.INTER_AREA)
# image_to_ascii(Image.fromarray(small_img))


# cv.waitKey(0)







