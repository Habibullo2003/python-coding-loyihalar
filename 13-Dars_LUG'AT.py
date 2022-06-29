# dasturchi = {
#     'ism' : 'Doniyor',
#     'kasbi' : 'dasturchi',
#     'yoshi' : 25,
#     'yo\'nlishi' : 'beckend'
# }

# print(dasturchi)
# print(dasturchi.items())

# avto = {
#     'anvar' : 'ferrari',
#     'dilshod' : 'tesla',
#     'doston' : 'Damas',
#     'nurbek' : 'Spark'
#     }

# for kalit, qiymat in avto.items():
#     print(f"{kalit.title()}ning mashinasi, {qiymat} \n")
    
# ismlar = {
#     'Fazliddin' : 'Samarqand',
#     'Zubaydulllo' : 'Fargona',
#     'Anvar'  :  'Qashqadaryo',
#     'Doston' : 'Xorazm',   
#     'Nurbek' : 'Andijon'
# }
# print("Ismlar ro'yxati")
# for kalit in ismlar.keys():      #keys metodi faqat kalit so'zlarni chiqarib beradi.
#     print(f"{kalit.title()}")

# ruyxat = {
#     'banan' : 20000,
#     'olma'  : 15000,
#     'anor'  : 18000,
#     'nok'   : 23000,
#     'behi'  : 25000
# }
# buyurtma = ['banan', 'nok', 'shaftoli', 'qulupnay', 'gilos']
# for mijoz in buyurtma :
#     if mijoz in ruyxat:
#         print(f"{mijoz.title()} bor, {ruyxat[mijoz]} so'm ")
#     else:
#         print(f"bu mahsulotlar bizda yo'q!, {mijoz.title()}")

# doslarim = {
#     'alisher' : 'redmi',
#     'husniddin' : 'iphone',
#     'doston' : 'samsung',
#     'fazliddin' : 'redmi',
#     'odil' : 'samsung',
#     'mansur' : 'realmi',
#     'anvar' : 'iphone' 
# }
# print("Mening do'stlarim quyidagi telefon modellarini ishlatishadi: ")
# for doslar in doslarim.values():
#     print(doslar.title())

# doslarim = {
#     'alisher' : 'redmi',
#     'husniddin' : 'iphone',
#     'doston' : 'samsung',
#     'fazliddin' : 'redmi',
#     'odil' : 'samsung',
#     'mansur' : 'realmi',
#     'anvar' : 'iphone' 
# }
# print("Mening do'stlarim quyidagi telefon modellarini ishlatishadi: ")
# for doslar in set(doslarim.values()):
#     print(doslar.title())

# doslarim = {
#     'alisher' : 'redmi',
#     'husniddin' : 'iphone',
#     'doston' : 'samsung',
#     'fazliddin' : 'redmi',
#     'odil' : 'samsung',
#     'mansur' : 'realmi',
#     'anvar' : 'iphone' 
# }
# print()
# for doslar in sorted(doslarim):
#     print(doslar.title())

           #HOMEWORK
# Izohli lug'at yarating va lug'atga kamida 10,15 ta so’z qo’shib. Lug'atdagi har 
#bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida qilib konsolga 
#chiqaring. 
# futbolchilar = {
#     'Ronaldo' : 7,
#     'Curtuva' : 1,
#     'Ramos' : 4,
#     'Marselo' : 12,
#     'Bale' : 11,
#     'Modrich' : 10,
#     'Kross' : 8,
#     'Casemiro' : 14,
#     'Varan' : 5,
#     'Vinisius' : 20,
#     'Benzema' : 9,
#     'Rodrigo' : 21,
#     'Isko' : 22,
#     'Carvahal' : 2,
#     'Militao' : 3
# } 
# print(f"Real madrid Futbolchilari ro'yxati: ")
# for kalit, qiymat in sorted(futbolchilar.items()):
#     print(f"{kalit}, raqami {qiymat}")

#Taniqli shaxslar va ularning tug’ilgan yili lug'atini tuzing. Avval lug'atdagi
#shaxslarning ismi-familyasi, keyin tug’ilgan yilini, alohida-alohida, alifbo
#ketma-ketligida konsolga chiqaring. 
# T_shaxslar = {
#     'Ronaldo' : 1985,
#     'Ramos' : 1986,
#     'Messi' : 1987,
#     'Mbappe' : 1999
# }
# print('Taniqli shaxslar va ularning tug\'ilgan yili: ')
# for kalit, qiymat in sorted(T_shaxslar.items()):
#     print(f"{kalit} {qiymat} - yilda tug'ilgan. ")

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning
#poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
#“Bizning lug’atda bunday davlat yo'q" degan xabarni chiqsin!
#            
# davlat = input("davlat nomini kiriting:\n ")
# davlatlar = {
#     'o\'zbekiston' : 'toshkent',
#     'portugaliya' : 'lissabon',
#     'angliya'  :  'lonndon',
#     'rossiya' : 'moskva',
#     'uels' : 'kardiff' 
# }
# if davlat in davlatlar.keys():
#     print(davlatlar[davlat].title())
# else:   
#     print('Siz kiritgan davlat bizning ro\'yxatda topilmadi')

#FASTFOOD menusi lug'atini tuzing (menyuda kamida 10 ta taom va narh juftligini
#kiriting). Foydalanuvchidan 5-ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan
#taomlarni menyu bilan solishtiring, agar taom menyuda bo'lsa narhini ko'rsating, taom
#menyuda bo’lmasa “kechirasiz bizda bunday taom yo'q" degan xabarni chiqsin.
# fastfood = {
#     'osh' : 17000,
#     'qozonkabob' : 37000,
#     'beshbarmoq' : 23000,
#     'gumma' : 10000,
#     'somsa' : 7000,
#     'kabob' : 25000,
#     'mastava' : 20000,
#     'kifsi' : 23500,
#     'jarkob' :18000,
#     'tuxumbarag' : 15000
# }
# for buyurtma in range(1,6):
#     buyurtma = input("ovqat nomini kiriting: ")
#     if buyurtma.lower() == fastfood.keys():
#         print(buyurtma.values())
#     else:
#         print("kechirasiz bizda bunday taom yo'q!")