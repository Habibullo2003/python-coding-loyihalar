# x = 7
# y = 7.7
# z = 1j
# print(type(x))
# print(type(y))
# print(type(z))              #elementlarni  tipini chiqarib beradi.   

# x, y, z = 10, -7.25, -30
# print(x,y,z)

# telefon_nomer = 94_335_25_27
# print(f"mening telefon nomerim, {telefon_nomer}")

# ism = 'Alisher'
# yosh = 18
# xabar = ism + ' ' + str(yosh) + ' ' + 'yoshda'
# print(xabar)

# t_yil = int(input("tug'ilgan yilingizni kiriting:"))
# yosh = 2022 - t_yil
# print(" siz " + str(yosh) + " yoshdasiz ")

# qalamlar = ["qizil", "ko'k", "oq", "qora" ]
# kunlar = ["dushanba", "seshanba", "chorshanba", "payshanba"]
# print(qalamlar)
# print(kunlar)

# ismlar = ["Habibullo", "Alisher", "Davron", "Diyor"]
# mevalar = ["olma", "o'rik", "banan", "gilos"]
# print("Birinchi ism:", ismlar[0])
# print("to'rtinchi meva:", mevalar[3])

# ismlar = ["Habibullo", "Alisher", "Davron", "Diyor"]
# mevalar = ["olma", "o'rik", "banan", "gilos"]
# print("Birinchi ism:", ismlar[0].title())
# print("to'rtinchi meva:", mevalar[3].upper())

# narxlar = [10000, 15000, 20000, 25000]
# print(narxlar[0] + narxlar[3])

# gm = ["neksiya", "cobalt", "spark", "damas", "gentra", "matiz"]
# print(gm[-1])

# mevalar = ["olma","gilos","banan","o'rik"]
# mevalar.append("olcha")
# print(mevalar)

# cars = []
# cars.append("Lacetti")
# cars.append("Nexia 3")
# cars.append("cobalt")                 #append() oxiridan qiymat qo'shadi
# print(cars)

# mevalar = ["olma","gilos","banan","o'rik"]
# mevalar.insert(0, "olcha")
# print(mevalar)

# mevalar = ["olma","gilos","banan","o'rik"]
# mevalar.insert(3,"olcha")                               #insert()  indeks bo'yicha qiymat qo'shadi 
# print(mevalar)

# mevalar = ["gilos", "olcha", "banan", "o'rik"]
# del mevalar[3]                                          # del indeks bo'yicha o'chiradi
# print(mevalar)

# mevalar = ["olcha", "shaftoli", "behi", "banan"]
# mevalar.remove("shaftoli")                             #remove() element qiymati bo'yicha qiymat o'chiradi.
# print(mevalar)

# qalamlar = ["qora", "qizil", "ko'k", "yashil"]
# uquv_quroli = qalamlar.pop(2)                           #agar pop() deyilsa oxirgi element o'zlashtiriladi.
# print("Menga " + uquv_quroli + " qalam kerak")
# print("Menga " + uquv_quroli + " qalamlar kerak emas")

                 #HOMEWORK

a = int(input("sonni kiriting:"))
print("a sonining kvadrati", a**2, "ga teng")
print("a sonining kubi " , a**3, "ga teng")

a = int(input("sonni kiriting:"))
tugilgan_yilim = 2022 - a
print(tugilgan_yilim)

         # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting.

ismlar = ["Akobir","Azizbek","Javohir"]
print(ismlar)
         # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

names = ["Akobir qayerdasan?","Azizbek darsga kettingmi","Javohir nima gaplar?"]
print(names)
           #sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
numbers = ["7","-19","41","10"]
print(numbers)

           #Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi
            # ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.


numbers = ["7","-19","41","10"]
numbers.append("15")
print(numbers)

numbers = ["7","-19","41","10"]
numbers.insert(2,"72")
print(numbers)

sonlar = ["7","-19","41","10"]
del sonlar[3]
print(sonlar)

numbers = ["7","-19","41","10"]
numbers.remove("-19")
print(numbers)

numbers = ["7","-19","41","10"]
notebook = numbers.pop(2)
print("Menga " + notebook + " ta daftar kerak")
notebook = numbers.pop()
print("Menga " + notebook + " ta daftar kerak emas")

     #t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan
     #tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ["Amir Temur","Jaloliddin Manguberdi","Imom al-Buxoriy","Abu Ali ibn-Sino"]
print(t_shaxslar)
z_shaxslar = ["Erkin Vohidov","Bobur Bobomurod","Muhammad Ali Eshonqulov","Abdukarim Mirzayev"]
print(z_shaxslar)

t_shaxslar = ["Amir Temur","Jaloliddin Manguberdi","Imom al-Buxoriy","Abu Ali ibn Sino"]
alloma = t_shaxslar.pop(2)
print("Menga " + alloma + " asarlari yoqadi")
olim = z_shaxslar.pop(3)
print("Menga " + olim + " beradigan motivatsiyalari yoqadi")

       # Friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = ["Azizbek","Bobur","Samandar"]
friends.append("Doniyor")
friends.append("Nodirbek")
friends.append("Baxtiyor")
friends.append("Zafar")
friends.append("Xayrullo")
print(friends)

            # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamidao'chrib tashlang.
friends = ["Azizbek","Bobur","Samandar","Nodirbek","Baxtiyor"]
friends.remove("Bobur")
friends.remove("Baxtiyor")
print(friends)

            # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends = ["Azizbek","Nodirbek","Baxtiyor"]
friends.append("Bobur")
friends.insert(1,"Samandar")
friends.insert(0,"Javohir")
print(friends)

            # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari
            # yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
            # mehmonlar ro'yxatiga qo'shing.
friends = ["Azizbek","Nodirbek","Baxtiyor","Davron"]
mehmonxona = []
mehmonxona.append("Sardor")
mehmonxona.append(friends.pop(2))
print(mehmonxona)

