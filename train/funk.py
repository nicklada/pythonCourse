#глобальная переменная
shop_item = 'шоколад'

def createShoppingList():
    '''Создает список покупок из инпута'''
    shopping_list = []
    while True:
        #локальная переменная shop_item - переопределит ту которая за пределами функции
        shop_item = input('Что добавить в список? \n')
        if shop_item == 'все' or shop_item == 'ничего':
            break
        shopping_list.append(shop_item)
    return shopping_list

def printShoppingList(shopping_list):
    '''Выводит список покупок'''
    print('\nИтого купить: ')
    for i in shopping_list:
        print (i)

#параметры по умолчанию, ключевые параметры
def weightCalc(forkilo, weight = 1):
    price = weight * forkilo
    return price


#Переменное число параметров (кортеж)
def sumTotal(*price):
    total = 0
    for i in price:
        total += i
    return total


shopping_list = createShoppingList()
printShoppingList(shopping_list)

price_apple = weightCalc(100)
price_banana = weightCalc(70, 0.5)
print('Цена яблок - {} рублей, а бананов - {} рублей'.format(price_apple, price_banana))
final_price = sumTotal(price_apple, price_banana)
print('С вас {} рублей'.format(final_price))

#Строки документации
print(createShoppingList.__doc__)
#help(createShoppingList)