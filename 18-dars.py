# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 06:05:49 2023

@author: User
"""
# WHILE, RO'YXATLAR VA LUG'ATLAR
# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH
gullar=[]
print('Yoqtirgan gullaringiz ro`yxatini tuzamiz.')
n=1
while True:
    savol=f'{n}-yoqtirgan gulingiz:'
    gul=input(savol)
    gullar.append(gul)
    n+=1
    javob=input('Yana gul qo`shasizmi?(ha/yo`q)')
    if javob =='ha':
        continue
    else:
        break
print('Yoqtirgan gullaringiz ro`yxati:')
for gul in gullar:
    print(gul.title())

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

gullar_rang={}
print('Gullaringiz rangini saqlovchi ro`yxat tuzamiz.')
r=1
while True:
    gul_1=input(f'{r}-gul nomini kiriting:')
    rang=input(f'{gul_1.title()}nig rangini kiriting:')
    r+=1
    gullar_rang[gul_1]=rang
    javob=input('Yana gul nomi kiritasizmi?(ha/yo`q)')
    if javob =='yo`q':
        break
print('Yoqtirgan gullaringiz rangi ro`yxati:')
for k,v in gullar_rang.items():
    print(f'{k.title()}ning rangi {v} rangda')

# RO'YXAT ELEMENTLARINI O'CHIRISH

#Avvalgi darslarimizning birida ro'yxat elementini o'chirish uchun `
#.remove(qiymat)` metodi bilan tanishgan edik. Esingizda bo'lsa, bu metod ro'yxatdan 
#eng birinchi uchragan qiymatni o'chiradi. Agar ro'yxatimizda ma'lum bir qiymat bir necha 
#bor takrorlangan bo'lsa, ularning barchasini o'chirib tashlash uchun `while` 
#tsiklidan foydalanishmiz mumkin.

cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)

# Yuqoridagi tsikl toki `cars` degan ro'yxatda `'nexia'` qiymati tugagunga qadar takrorlanaveradi.

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
# Tasavvur qiling bizda ma'lum bir ro'yxat bor, biz ro'yxatdagi har bir 
# element ustida biror amalni bajarib, uni birinchi ro'yxatdan ikkinchi ro'yxatga 
# ko'chirib olmoqchimiz. Shunday holatlarda while tsikli juda qo'l keladi.

print('Ro`yxatdagi mashinalar rangi jadvalini tuzamiz.')
cars1=['lambo','ferrari','rolls roys','merc','bmw']
cars1_rang={}
while cars1:
    savol=cars1.pop()
    rang=input(f"{savol.title()}nig rangini kiriting:")
    print(f"{savol.title()}nig rangi qabul qilindi.")
    cars1_rang[savol]=rang
    
for a,b in cars1_rang.items():
    print(f'{a.title()}ning rangi {b} rangda.')
    




































