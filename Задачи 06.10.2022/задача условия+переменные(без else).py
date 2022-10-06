from unittest import result


name = input('Логин:')
pas = input('Пароль:')
if name == 'nikita' or pas == '135':
    result = 'Добро пожаловать!'
if not name == 'nikita' or not pas == '135':
    result = 'Не правильный логи или пароль.'
print(result)