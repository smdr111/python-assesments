# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 07:14:28 2023

@author: User
"""

# `input()` funktsiyasi ichidagi matn ingliz tilida prompt, savol deyiladi. 
# Aslida biz savolni ham o'zgaruvchiga yuklab, shaxsiy so'rovnomalar ham yaratishimiz mumkin.

joy=input('Qayerdan tug`ilgansiz?\n')
yil=int(input(f'Men O\'zbekistonlikman.{joy.title()} yaxshi davlat.\nNechanchi yilsiz?\n'))
yil_1=(f"{yil}-yilda tug`ilgan bo`lsangiz unda {2023-yil} yoshda ekansiz.")
print(yil_1)

#   SONLAR va INPUT()
# input() funktsiyasi har qanday kiritilgan qiymatni matn sifatida qabul qilib oladi. 
# Agar foydalanuvchidan son talab qilinsa, foydalanuvchi kiritgan qiymatni butun (integer) 
# yoki o'nlik (float) son ko'rinishiga o'tkazib olish kerak.
# Buning uchun int() yoki float() funktsiyalaridan foydalanamiz.
ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh) # yosh ni butun songa o'tkazamiz
height = input("Bo'yingiz necha metr? ")
height = float(height) # bo'yni o'nlik songa o'tkazamiz

# WHILE TSIKLI BILAN TANISHAMIZ
# Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir ro'yxatni olib, 
# ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni takrorlar edi. while ham takrorlash operatori bo'lib, 
# for dan farqli ravishda, toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi.
# while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.

son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end=' ') # son ni konsolga chiqaramiz,
    son = son+1 # songa 1 qo'shamiz.

# Pythonda += operatori bor. Bu operator o'ng tarafdagi qiymatni chap tarafdagi qiymatga qo'shadi. 
# Misol uchun, yuqorida son = son + 1 o'rniga son += 1 deb yozishimiz mumkin.

# while va input()
# Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarilayotgan edi. 
# while tsikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


# Ishora (flag)
# Yuqoridagi dasturda dasturni to'xtatish uchun yagona shartni tekshirdik (qiymat!='exit'),
# katta dasturlarda bir emas bir nechta shartlarni tekshirish, va ulardan biri bajarilgan taqdirda dasturni 
# to'xtatish talab qilinishi mumkin.

# Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin. 
# Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri bajarilganda ishora 
# o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
    
# `BREAK` OPERATORI
# `Break` operatori yordamida ma'lum bir shartni tekshirish va `while` tsikli 
# bajarilishini to'xtatib qo'yish mumkin. 

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)

# `Break` operatori `for`tsiklini to'xtatish uchun ham ishlatiladi.

sonlar = list(range(1,11))
for son in sonlar: 
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
# while tsikli ichida bir nechta break operatori ham bo'lishi mumkin.


# `CONTINUE` OPERATORI
# Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab 
# o'tish uchun mo'ljallangan.

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")
    
son = 0
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
#  `while` tsikli ichida bir nechta `continue` operatori ham bo'lishi mumkin.

# # ABADIY TSIKL TUZOG'I

# Tsikllar bilan ishlashda abadiy tsikl yaratib qo'yishdan ehtiyot bo'lishimiz kerak. 
# Abadiy tsiklga turli mantiqiy xatolar sabab bo'lishi mumkin: noto'g'ri shart, o'zgarmas qiymat, 
# kodlar ketma-ketligida xatolik va hokazo. 

# Keling ba'zi misollarni ko'ramiz:
# infinite loop
son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)
        
son = 1
while son>0: 
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
# Yuqoridagi kodda esa xato shart tufayli (son>0) kod abadiy aylanadi.

# DIQQAT! Abadiy tsikl bajarilishini to'xtatish uchun konsolda Ctrl+C tugmasini bosing






















