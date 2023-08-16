class DataIsEmpty(Exception):
      def __init__(self, data):
            self.data = data

class ShopAssistant:
   #переменная класса
    shop_amount = 0
    def __init__(self, name, city):
        self.name = name 
        self.city = city
        ShopAssistant.shop_amount+=1

    def createShoppingList(self):
        '''Создает список покупок из инпута'''
        shopping_list = []
        while True:
            #локальная переменная shop_item - переопределит ту которая за пределами функции
            shop_item = input('Что добавить в список? \n')
            if not shop_item:
                raise DataIsEmpty('Список не может быть пустым')
            elif shop_item == 'все' or shop_item == 'ничего':
                break
            else: shopping_list.append(shop_item)
        return shopping_list

    def printShoppingList(self, shopping_list):
        '''Выводит список покупок'''
        print('\nИтого купить: ')
        for i in shopping_list:
            print (i)