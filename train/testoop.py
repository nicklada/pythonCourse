import oop_1
import oop_2

#создать и вывести список покупок
assistant = oop_1.ShopAssistant('Manya', 30)
try:
    mylist = assistant.createShoppingList()
    assistant.printShoppingList(mylist)
    #посчитать стоимость покупок
    calk = oop_2.ShoppingCalc('semishagoff')
except oop_1.DataIsEmpty as e:
    print(e)


apple_price = calk.weightCalc(20, weight = 0.5)
banana_price = calk.weightCalc(60)
sum = calk.sumTotal(apple_price, banana_price)
print('С вас {} рублей'.format(sum))
