"""
username = input('請輸入帳號: ')
password = input('請輸入密碼: ')
# 如果希望輸入口令時 終端中沒有回顯 可以使用getpass模塊的getpass函數
# import getpass
# password = getpass.getpass('請輸入口令: ')
if username == 'admin' and password == '123456':
    print('身份驗證成功!')
else:
    print('身份驗證失敗!')
"""

from random import randint

face = abs(randint(-6, 6))

if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳個舞'
elif face == 3:
    result = '學狗叫'
elif face == 4:
    result = '做俯臥撐'
elif face == 5:
    result = '念繞口令'
elif face == 0:
    result = '1/13'
else:
    result = '講冷笑話'
print('%s %d' % (result,face))












