# kun = input("kunni kiriting: ")
# if kun.lower() == "shanba"  or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("bugun dars kuni")

# kun = input("Bugun kun nima: ")
# harorat = input("Bugun havo harorati qanday:")
# if (kun.lower() == "yakshanba" and kun.lower() == "shanba") and harorat > 30:
#     print("Cho'milgani kettik")
# else:
#     print("Bugun cho'milmaymiz!")
# oshxona = ['manti','somsa','sho\'rva','kabob']
# ovqat = input("Nima ovqat yeysiz?=")
# if ovqat.lower() in oshxona:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Afsuski bo ovqat bizda mavjud emas!")

# oshxona = ['manti','somsa','sho\'rva','kabob']
# ovqat = input("Nima ovqat yeysiz?=")
# if ovqat.lower() not in oshxona:
#     print("Afsuski bu ovqat bizda mavjud emas!")
# else:
#     print("Buyurtmangiz qabul qilindi")

# oshxona = ['osh', 'mastava', 'manti','sho\'rva'] 
# ovqat = ['qozonkabob','norin','kabob','jarkob']
# for taom in ovqat:
#     if taom not in oshxona:
#         print(f"Kechirasi menuda {taom} yo'q")
#     else:
#         print(f"Menuda {taom} bor") 

# oshxona = ['osh', 'mastava', 'manti','sho\'rva'] 
# ovqat = [] 
# if ovqat:
#     for taom in ovqat:
#         if taom in oshxona:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Menuda {taom} yo'q ")

# phone = {'model':'Galaxy A52S', 'rangi':'qora','operativka':'8 gb','xotira':'128 gb'}
# print(phone['model'])
# print(phone['rangi'])
# print(phone['operativka'])
# print(phone['xotira'])

# talaba = {'ism':'Habibullo',   'familiyasi':'Xayrullayev',   'yoshi':19,  'universiteti':'TATU','kursi':1,'fakultet':'K.I.F'}
# print(f"{talaba['ism'].title()} ")
# print(f"{talaba['familiyasi'].title()}")
# print(f"{talaba['yoshi']}- yoshda")
# print(f"{talaba['universiteti']} da o'qiydi")
# print(f"{talaba['kursi']}- kursda o'qiyapti")
# print(f"{talaba['fakultet'].upper()}")

# talaba = {'ism':'Habibullo',   'familiyasi':'Xayrullayev',   'yoshi':19,  'universiteti':'TATU','kursi':1,'fakultet':'K.I.F'}
# print(f"""
# "{talaba['ism'].title()} ,
# {talaba['familiyasi'].title()},
# {talaba['yoshi']}- yoshda,
# {talaba['universiteti']} da o'qiydi,
# {talaba['kursi']}- kursda o'qiyapti,
# {talaba['fakultet'].upper()}". 
# """)


      #Homework
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa
#"Bu son juft emas" degan xabarni chiqaring.
# son = int(input("juft sonni kiriting: "))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas!")
 
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#• Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#• Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#• Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input("yoshingizni kiriting: "))
# if yosh < 4 and yosh > 60:
#     print("Kirish bepul")
# elif yosh < 18:
#     print("Kirish 10000 so'm")
# else:
#     print("Kirish 20000 so'm")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida
#xabarni chiqaring.
# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a, '>', b)
# elif b < a:
#     print(b, '>', a)
# else:
#     print(a, '==', b)

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat
#yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, 
#mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
#"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["anor","uzum","kartoshka","piyoz","sabzi","olma","anjir","banan","o'rik","shaftoli"]
# savat = []
# for  n  in range(1,3):
#     savat.append(input(f"{n} - mahsulot nomini kiriting: "))   
#     if savat not in mahsulotlar:
#         print("Mahsulot ", savat, " do'konimizda bor")
#     else:
#         print("Mahsulot ", savat, " do'konimizda yo'q")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha
#bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
n = int(input("n= "))
if n%2 == 0 or n%3 == 0 or n%4 == 0 or n%5 == 0 or n%6 == 0 or n%7 == 0 or n%8 == 0 or n%9 == 0 or n%10 == 0:
    print(n, "soni qoldiqli bo'lindi")
else:
    print(n , "soni qoldiqli bo'linmaydi")