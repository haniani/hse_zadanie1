# -*- coding: utf-8 -*-
# для работы необходим исходный текст + файл алфавита
import os, fileinput

file = open('al.txt') # таблица значений
dr = {}
ar = []

for line in file: ### обходим файл
    line = line.strip('\n') # убрать переносы
    line = line.split('\t') # разбиваем на массивы
    ar.append(line)

for i in range(len(ar)): # обходим массив (i - строки)
    #print(ar[i])
    for x in range(len(ar[i])): # x - номер элемента в строке
        if i != 0 and x != 0: # исключаем обработку ключа
            j = ar[i][x]
            m = ar[0][x] + ar[i][0] # m - слог, состоящий из номера строки и номера элемента
            dr[j] = m # генерируем словарь

def transliterate(string):
    for i, j in dr.items():
        string = string.replace(i,j)
    return string



with fileinput.FileInput('texta.txt', inplace=True, backup='.bak') as file:
    for line in file:
        print(transliterate(line), end='')
