import smtplib
from email.mime.text import MIMEText
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('yoonhyun0707@gmail.com', 'oyrcuokrjlvybbqt')
msg = MIMEText("내용 : ㅎㅇ")
msg['subject'] = '제목 : 실험'
s.sendmail("yoonhyun0707@gmail.com", "asunmia@gmail.com", msg.as_string())
s.quit() 
print("The mail successfully sent") 