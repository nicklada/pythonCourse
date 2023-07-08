#!/usr/bin/env python3
def reverse(text): 
    return text[::-1]

def is_palindrome(text):
    forbiden = (' ', ',', '!', '?', '.')
    replaced = reverse(text)
    for i in forbiden:
            if i in text:
               text =  text.replace(i, '')
            if i in replaced:
                replaced = replaced.replace(i, '')

    if text == replaced:
        print("Да, это палиндром")
    else:
        print("Нет, это не палиндром")

def getText():
   text = input('Введите текст: ')
   return text

something = getText()
is_palindrome(something)
