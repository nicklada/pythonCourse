while True:
    password = input('Введите пароль: ')
    
    if password == 'pass':
        print('Верно! Заходите')
        break
    elif password == 'зфыы':
        print('Переключитесь на англ')
        continue
    else:
        print('Неверный пароль')