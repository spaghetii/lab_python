
"""
a = 321
b = 123
# +,-,*,/,mod
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
# 取商值
print(a // b)
# 指數
print(a ** b)
"""
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
"""
"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # int
print(type(b)) # float
print(type(c)) # complex
print(type(d)) # str
print(type(e)) # bool
"""
"""
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
"""
"""
import math

radius = float(input('請輸入圓的半徑: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周長: %.2f' % perimeter)
print('面積: %.2f' % area)
"""

year = int(input('請輸入年份: '))
# 如果代碼太長寫成一行不便於閱讀 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)




