import cv2 as cv
from PIL import Image

video = cv.VideoCapture(0)

def resize(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv.resize(frame, (width, height))


ascii_chars = """&@WM%8D#b$0NqGXOEyVS2xCj}t?lv^i/r7<+!*~";_:,'-.`"""

def image_to_ascii(image):
    pixels = image.getdata()
    characters = []
    for pixel in pixels:
        characters.append(ascii_chars[pixel//int(255/len(ascii_chars) + 1)])
    characters = "".join(characters)

    pixel_count = len(characters)
    ascii_image = []
    for i in range(0, pixel_count, 200):
        ascii_image.append(characters[i:i+200])
    ascii_image = "\n".join(ascii_image)

    print(ascii_image)
    # with open("ascii_image.txt", "w") as f:
    #     f.write(ascii_image)

while True:
    isTrue, frame = video.read()
    # frame = cv.imread("cat.jpg")

    ratio = frame.shape[0]/frame.shape[1]

    small_img = cv.resize(frame, (200, int(ratio * 200)), interpolation=cv.INTER_AREA)

    # cv.imshow("Small Cat", small_img)

    gray = cv.cvtColor(small_img, cv.COLOR_BGR2GRAY)
    # cv.imshow("Gray", gray)

    image_to_ascii(Image.fromarray(gray))


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()

cv.waitKey(0)

