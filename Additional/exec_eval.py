#!/usr/bin/env python3
action = '''
for i in range (1, 5):
    print(i+1, end=' ')
'''
print(exec(action))   #2 3 4 5 None

expression = "(1+8)/3"
print(eval(expression))   #3.0