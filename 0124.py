import random
s = 0
print("Add all numbers that printed out and enter the sum of numbers")
for i in range(3):
    x = random.randrange(1, 101)
    s += x
    print(x)
z = 1
while z != s:
    y = int(input("put your number : "))
    if y == s:
        print("correct")
        break
    else:
        print("wrong")


# import smtplib
# from email.mime.text import MIMEText
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login('yoonhyun0707@gmail.com', 'oyrcuokrjlvybbqt')
# msg = MIMEText("내용 : ㅎㅇ")
# msg['subject'] = '제목 : 실험'
# s.sendmail("yoonhyun0707@gmail.com", "asunmia@gmail.com", msg.as_string())
# s.quit() 
# print("The mail successfully sent") 















