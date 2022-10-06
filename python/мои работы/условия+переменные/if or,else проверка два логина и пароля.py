myname = input('Введите логин: ')
mypass = input('Введите пароль: ')
if (myname == '123' and mypass == 'qwe') or (myname == '234' and mypass == 'asd'): 
    result = 'Добро пожаловать, о великий хакер!'
else:
    result = 'Ты кто такой, давай до свидания...'
print(result)
