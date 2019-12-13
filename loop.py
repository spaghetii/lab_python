"""
# range(101) = 0~100
# range(1,100) = 1~99
# range(1,100,2) = 1~99 (step by 2)
sum = 0
for x in range(101):
    sum += x
print(sum)
"""
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商餘額明顯不足')
"""
"""
for i in range(1, 10):
    for j in range(1, 10):
        print('%d*%d=%s' % (i, j, str(i * j).zfill(2)), end='\t')
    print()
"""
"""
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x # swap
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公約數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break
"""
# 水仙花數
""" part1
x=int(input('input three digits (if you input more than three digits,it will get last three digits)\n'))
x%=1000
first=x//100
middle=(x//10)%10
last=x%10
if x==(first**3)+(middle**3)+(last**3):
    print('%d is Narcissistic number'%x)
else:    
    print("%d isn't Narcissistic number"%x)
"""
"""part2
for first in range(10):
    for middle in range(10):
        for last in range(10):
            sum=(first*100+middle*10+last)
            if sum==(first**3)+(middle**3)+(last**3):
                print('%d is Narcissistic number'%sum)
"""
# 費氏數列
def fib(n):
        a, b = 1, 1
        for i in range(n):
            if i%10==0:
                print()    
            print('f(%d) = %d'%(i,a), end=' ')
            a, b = b, a+b
fib(100) 







