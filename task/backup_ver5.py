#!/usr/bin/env python3
import os
import time
import zipfile
import sys
# Имена файлов/каталогов для сжатия передаем в качестве аргументов в командной строке
# при запуске скрипта
names = sys.argv[1:]
print(names)

# Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['/Users/lada/tmp/py/functions', '/Users/lada/tmp/py/modules']
# К ним добавляем имена каталогов переданные в качестве аргументов при запуске
source.extend(names)
print(source)

# Прописываем директорию, где будет архив
target_dir = '/Users/lada/tmp/py/task/backup'

# Именем для директории zip-архива служит текущая дата.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Именем для zip-архива служит текущее время
now = time.strftime('%H%M%S') 

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: 
    target = today + os.sep + now + '.zip' 
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Создаём директорию для архива, если ее ещё нет
if not os.path.exists(today): 
    os.mkdir(today)
    print('Каталог успешно создан', today)

# Создаем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)

# Запускаем создание резервной копии в архиве по указанной директории
def makezip():
    try:
        with zipfile.ZipFile(target, 'w') as zipf:
            zipf.debug = 3
            for directory in source:
                zipf.write(directory)
        print('Создание резервной копии выполнено успешно')
    except zipfile.BadZipfile:
        print('Создание резервной копии не удалось')

makezip()