#!/usr/bin/env python3
#percent = 10 это значение параметра по умолчанию
def creditcalk(sum, percent = 10):
    print ('Переменная sum изначальна равна', sum)
    sum = sum + (sum/100)*percent
    print('Сумма кредита равна ', sum)

#в этом случае значение параметра percent будет по умолчанию = 10
creditcalk(1000)
#в этом случае значение параметра percent будет =5
creditcalk(1000, 5)
