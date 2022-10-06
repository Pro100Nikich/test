from unittest import result


name = input('Логин: ')
pas = input('Пароль: ')
if name ==  'nikita' and pas == '135':
    result = 'Добро пожаловать!'
else:
    result = 'Не правильный логин или пароль'
print(result)