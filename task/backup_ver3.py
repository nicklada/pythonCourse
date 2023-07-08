#!/usr/bin/env python3
import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['/Users/lada/tmp/py/functions', '/Users/lada/tmp/py/modules']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать # двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва. 
target_dir = '/Users/lada/tmp/py/task/backup'
# 3. Файлы помещаются в zip-архив.

# 4. Именем для директории zip-архива служит текущая дата.
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

# Создаём директорию, если ее ещё нет
if not os.path.exists(today): 
    os.mkdir(today)
    print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', today)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')