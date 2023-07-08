#!/usr/bin/env python3
import time

content = '''I got new rules, I count 'em
I got new rules, I count 'em
I gotta tell them to myself
I got new rules, I count 'em
I gotta tell them to myself
'''

try:
    f = open('song.txt', 'w')
    f.write(content)
    f.close()
    f = open('song.txt', 'r')
    while True:
      line = f.readline()
      print(line)
      if len(line) == 0:
          break
      time.sleep(2)
except KeyboardInterrupt:
    print('Вы отменили чтение файла')
finally:
    f.close()
    print('Файл закрыт')