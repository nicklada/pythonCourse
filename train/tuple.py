#tuple
def createGuestTuple(*names):
    '''Создает неизменяемый список гостей на пати
    Это кортеж - следовательно, добавлять по одному имени нельзя'''
    party_list = (names)
    return party_list


def printGuestList(party_list):
    '''Выводит список гостей'''
    print('\nНа пати приглашены: ')
    for i in party_list:
        print (i)

#будет вызывать падение, т.к. кортеж неизменяемый
def changeGuestList(name, party_list):
    party_list.__add__(name)

def getGuestsByIndex(party_list, index1, index2):
    name = party_list[index1:index2]
    print('По указанному индексу расположен {}'.format(name))
    
myparty = createGuestTuple('yarik', 'ladka', 'grisha', 'papa', 'mama')
printGuestList(myparty)

#выдаст элементы с индексом 1-4 (вырезка от 1 до 5(невключительно))
getGuestsByIndex(myparty, 1, 5)

#упадет с ошибкой, т.к. кортеж неизменяемый
#newparty = changeGuestList('Petya', myparty)
