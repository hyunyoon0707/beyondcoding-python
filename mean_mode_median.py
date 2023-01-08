import time

x = list(map(int,input().split()))




def mean(a):
    
    s = 0
    for i in a:
        s += i
    return s/len(a)
def median(b):
    a = sorted(b)
    if len(a) % 2 == 0:
        return (a[len(a)//2-1] + a[len(a)//2]) / 2
    else:
        return a[len(a)//2]

def mode(b):
    a = sorted(b)
    p = []
    for i in a:
        p.append(a.count(i))

    if max(p) == 1 and len(p) != 1:
        return "\n\033[31mmode does not exist in your data\033[0m"
    elif max(p) == 1 and len(p) == 1:
        return a[p.index(max(p))]
    else:
        return a[p.index(max(p))]


def deviation(a,b):
    
    s = []
    for i in a:
        s.append(i-b)
    
    return s

def variance(a):
    s = 0
    for i in a:
        s += i**2
    
    return s/len(a)

def standard_deviation(a):
    return a **(1/2)


s = [' is mean of your data',' is median of your data',' is your mode of your data']


print(f"\n\033[31m{mean(x)}\033[0m is mean of your data")
time.sleep(0.7)
print(f"\n\033[31m{median(x)}\033[0m is median of your data")
time.sleep(0.7)
if type(mode(x)) == str:
    print(mode(x))
else:
    print(f"\n\033[31m{mode(x)}\033[0m is mode of your data")

time.sleep(0.7)
print(f"\n\033[31m{deviation(x,mean(x))}\033[0m is deviation of your data")
time.sleep(0.7)
print(f"\n\033[31m{variance(deviation(x,mean(x)))}\033[0m is variance of your data")
time.sleep(0.7)
print(f"\n\033[31m{standard_deviation(variance(deviation(x,mean(x))))}\033[0m = \033[31mroot {variance(deviation(x,mean(x)))}\033[0m is your standard_deviation of your data")





