#!/usr/bin/env python3
#простая генерация списка от 1 до 9
listgen = [i for i in range(1, 10)]
print(listgen) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# создать новый список на основе предыдущего, в котором каждый элемент 
#будет умножен на 2, кроме элемента который = 2
list = [1, 2, 3]
list2 = [i*2 for i in list if i != 2]
print(list2) #[2, 6]

#Генерация списка четных чисел от 1 до 20
listchet = [i for i in range(1, 20) if i%2 == 0]
print(listchet) #[2, 4, 6, 8, 10, 12, 14, 16, 18]

#Генерация списка букв слова
name = 'Nikolaeva'
liststr = [i for i in name]
print(liststr) #['N', 'i', 'k', 'o', 'l', 'a', 'e', 'v', 'a']