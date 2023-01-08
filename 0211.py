# s = 0
# x = input()

# list_1 = list(x)


# while 'l' in list_1:
#     list_1.remove('l')
#     s += 1

s = []
sss = []
zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
for i in range(3):
    x = int(input())
    s.append(x)

y = int(s[0])*int(s[1])*int(s[2])
ss = list(str(y))



while '0' in ss:
    ss.remove('0')
    zero += 1
sss.append(zero)


while '1' in ss:
    ss.remove('1')
    one += 1
sss.append(one)
while '2' in ss:
    ss.remove('2')
    two += 1
sss.append(two)
while '3' in ss:
    ss.remove('3')
    three += 1
sss.append(three)

while '4' in ss:
    ss.remove('4')
    four += 1
sss.append(four)
while '5' in ss:
    ss.remove('5')
    five += 1
sss.append(five)
while '6' in ss:
    ss.remove('6')
    six += 1
sss.append(six)

while '7' in ss:
    ss.remove('7')
    seven += 1
sss.append(seven)
while '8' in ss:
    ss.remove('8')
    eight += 1
sss.append(eight)
while '9' in ss:
    ss.remove('9')
    nine += 1
sss.append(nine)

for i in range(0, len(sss)):
    print(sss[i])






