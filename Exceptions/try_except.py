#!/usr/bin/env python3
try:
   text = input('Введите что-нибудь: ')
#End-of-file error если вводим ctrl-d думает, что это символ конца файла, 
# а его мы не ожидаем --> Python кидает EOFError
except EOFError:
    print('Зачем вы мне ввели ctrl-d?''\n''Я не ожидаю символа конца файла!')
# при вводе ctrl-c Python выкидывает KeyboardInterrupt
except KeyboardInterrupt:
    print ('Вы ввели ctrl-c и отменили операцию')
#если надо чтобы прога не падала при любом исключении
# пишем обработку для материнского класса Exception (от него все исключения наследуются)
except Exception:
    print('Возникло какое-то исключение')
#выполняется если ни одного исключения не возникло, пишем в else что должно быть сделано
else:
    print('Вы ввели {}'.format(text))