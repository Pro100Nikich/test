from xml.etree.ElementPath import xpath_tokenizer_re


myname = input('Введите логин: ')
mypass = input('Введите пароль: ')
if myname == '123' and mypass == 'qwe': 
    result = 'Добро пожаловать, о великий хакер!'
else:
    result = 'Ты кто такой, давай до свидания...'
print(result)
