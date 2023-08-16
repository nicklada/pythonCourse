class ShoppingCalc:
   #переменная класса
    def __init__(self, shopname):
        self.shopname = shopname 

    def weightCalc(self, forkilo, weight = 1):
        try:
            price = forkilo * weight
            return price
        except TypeError:
            print('Введите число!')
    
    def sumTotal(self, *price):
        try:
            total = 0
            for i in price:
                total += i
            return total
        except TypeError:
            print('Цена должна быть в формате числа!')