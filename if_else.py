# ism = "Habibullo"
# print(ism == "habibullo")

# ism = "Habibullo"
# print(ism == "Habibullo")

# ism = "Habibullo"
# print(ism !="habibulo")

# ism = "Habibullo"
# print(ism != "Habibullo")

# son = 15
# print(son == 15)

# son == 7
# print(son != 7)

# ism = input("Ismingizni kiriting: ")
# if ism.lower() == "habibullo":
#     print(f"Xush kelibsiz {ism}!")
# else:
#     print(f"Uzr {ism} biz habibulloni kutgandik!")

# ism = input("Ismingizni kiriting: ")
# if ism.lower() != "habibullo":
#     print(f"{ism} siz adashtingiz!")
# else:
#     print(f"{ism} siz to'g'ri topdingiz!")

# son = float(input("7*7 nechchiga teng: "))
# if son != 49:
#     print("Xato javob! yana urinib ko'ring!")
# else:
#     print("To'g'ri javob berdingiz! Ofarin! ")

# ism = [15, 17, 37, 48, 56,90,100]
# if ism[3] == 48:
#     print("To'g'ri javob!")
# else:
#     print("Noto'g'ri javob:")

# number = int(input("Sonni kiriting:"))
# if number >= 18:
#     print("True")
# else:
#     print("False")

# login = input("Yangi login kiriting:")
# if len(login) != 5:
#     print("XATO! Login eng kamida 5 ta belgidan iborat bo'lishi kerak")
#     print("Yana urinib ko'ring")
# else:
#     print("siz loginni to'g'ri kiritingiz:")
#     print(f"Xush kelibsiz {login} ")

# number = int(input("Sonni kiriting:"))
# if 2022 - number >= 18:
#     print("sizga kirishga ruxsat bor")
# else:
#     print(f"kechirasiz sizga kirishga ruxsat yo'q. chunki yoshingiz {2022 - number} da ekan")

# yosh = int(input("yoshingizni kiriting: "))
# if yosh < 5:
#     print("Sizga kirish bepul")
# elif yosh < 12:
#     print("Sizga kirish 5000 so\'m")
# elif yosh >= 65:
#     print("siz pensionersiz sizga kirish bepul:")
# else:
#     print("Sizga kirish 10000 so\'m")

# yosh = int(input("yoshingizni kiriting: "))
# if yosh < 5:
#     narxi = 0
# elif yosh < 12:
#     narxi = 5000
# else:
#     narxi = 10000
# print(f"Sizga kirish {narxi} so'm ")

# kun = input("kunni kiriting: ")
# if kun.lower() == "shanba"  or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("bugun dars kuni")

# kun = input("Bugun kun nima: ")
# harorat = input("Bugun havo harorati qanday:")
# if kun.lower() == "yakshanba" and kun.lower() == "shanba" and harorat > 30:
#     print("Cho'milgani kettik")
# else:
#     print("Bugun cho'milmaymiz!")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab
 #konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.


son = int(input("sonni kiriting: "))
if son > 0:
     print(son ** 0.5)
else:
    print("Musbat son kiriting:")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
number = int(input("sonni kiriting: "))
if number < 0:
    print("Manfiy son")
else:
    print("Musbat son")

# Foydalanuvchi login ismini so'rang. Agar login boshliq bo'lsa, ".Xush kelibsiz boshliq, Bugun
#ishga kegan ishchilarni ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush
#kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("loginni kiriting:")
if login == "boshliq":
    print("Xush kelibsiz boshliq, Bugun ishga kegan ishchilarni ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz, {login}!")
 
 # Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
login = input("loginni kiriting:")
if login != "boshliq":
    print("Xush kelibsiz, {login}!")    
else:
    print("Xush kelibsiz boshliq, Bugun ishga kegan ishchilarni ro'yxatini ko'rasizmi?")

# Yangi sohalar= [‘shifokor', ‘oqituvchi', ‘dasturchi', ‘usta', ‘diplomat’, ‘jurnalist’] degan ro'yxat
#tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. DASTURCHI
#uchun barcha harfni katta qiling.
Yangi  = ['shifokor', 'oqituvchi', 'dasturchi', 'usta', 'diplomat', 'jurnalist']
