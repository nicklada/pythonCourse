#!/usr/bin/env python3

class DataIsEmpty(Exception):
    pass
class DataIsOne(Exception):
    pass

def dataprocess(data):
    if not data:
        raise DataIsEmpty("Не было переданно данных")

    if data == 1:
        raise DataIsOne("AAAAAAA")
    
    else: 
        data += 10
        print(data)

try:
    data = []
    dataprocess(data)
except DataIsEmpty as e:
    print(str(e))
except DataIsOne:
    data = 2
    print(data)