class Admin():
    def __init__(self, name, age):
        self.name = name #переменная объекта
        self.age = age   #переменная объекта

    def createUserList(self):
        users = []
        while True:
            user = {}
            login = input('Создайте логин\n')
            if login == 'exit':
                break
            password = input('Создайте пароль\n')
            user["login"] = login
            user["password"] = password
            users.append(user)
        return users

    def printUserList(self, users):
        '''Выводит список юзеров'''
        print('\nВсе юзеры: ')
        for i in users:
            print (i)


    def getPassworsByLogin(self, users, login):
        for i in range(0,len(users)):
            if users[i]["login"] != login:
                continue
            else:
                password = users[i]["password"]
                print('Пароль:', password)

    def getUserByIndex(self, users, index):
        user = users[index]['login']
        print('По указанному индексу находится пользователь {}'.format(user))


Lada = Admin('Lada', 29)
users = Lada.createUserList()
Lada.printUserList(users)
Lada.getUserByIndex(users, 1)
Lada.getPassworsByLogin(users, 'ladka')
