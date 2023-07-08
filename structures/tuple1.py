#!/usr/bin/env python3
zoo = ('bear', 'pig', 'tiger')
print('Количество животных в зоопарке - ', len(zoo))

newzoo = ('cat', 'dog', zoo)
print('Количество клеток в зоопарке - ', len(newzoo))
print('Все животные в новом зоопарке:', newzoo)
print('Все животные из старого зоопарка:', newzoo[2])
print('Последнее животное, привезённое из старого зоопарка - ', newzoo[2][2])
print('Количество животных в новом зоопарке', len(newzoo)-1 + len(zoo))