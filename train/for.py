shoppinglist = []
while True:
    shopitem = input('Что добавить в список? \n')
    if shopitem == 'все' or shopitem == 'ничего':
        break
    shoppinglist.append(shopitem)

print('\nИтого купить: ')
for i in shoppinglist:
    print (i)