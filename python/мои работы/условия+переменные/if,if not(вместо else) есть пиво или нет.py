beer = input('Введи Yes, если пиво есть, и No, если пива нет: ')
if beer.lower() == 'yes':
    print('Пива нет!')
if not beer.lower() == 'yes':
    print('Ура, пиво еще есть!')