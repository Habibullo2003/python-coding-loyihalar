# #Ro'yxatlar bilan ishlash
# cars = ['bmv','mersedes benz','volvo','general motors','tesla', 'audi']
# print(cars)
# cars.sort()          #sort() funksiyasi ro'yxatni alifbo tartibida chiqarib beradi.
# print(cars)

# #Ro'yxatlar bilan ishlash
# cars = ['Bmv','mersedes benz','volvo','general motors','tesla', 'audi']
# print(cars)
# cars.sort()            #Katta harf qatnashsa birinchi katta harfli so'z keyin alifbo tartibida chiqadi
# print(cars)

# cars = ['bmv','mersedes benz','volvo','general motors','tesla','audi']
# print(cars)
# cars.sort(reverse = True)     #teskari tartibda chiqarib eradi
# print(cars)

# cars = ['bmv','mersedes benz ', 'general motors','audi','tesla']
# print(sorted(cars))           #ro'yxat asl holini o'zgartirmagan holda chiqarib beradi
# print(cars)

# number = [7, 8, 9, 10, 17]
# number.sort()
# print(number)
# print(sorted(number, reverse = True))

# fruits = ['lemon', 'banana', 'watermelon', 'apple', 'pear']
# fruits.reverse()       #reverse (). Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun.reverse() metodidan foydalanamiz.
# print(fruits)

# meva = ['ananas', 'gilos', 'olcha', "o'rik"]
# print("Ro'yxatni ichiodagi mevalar soni:", len(meva))   #Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
# sonlar = list(range(1,31))      # range() Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list()
#                                 # funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
# print(sonlar)

# sonlar = list(range(501))
# print(sonlar)

# juft_sonlar = list(range(0,31,2))
# toq_sonlar = list(range(1,32,2))
# print(juft_sonlar)
# print(toq_sonlar)

# narxlar = [10000, 13000,25000,28000,31000]
# arzon = min(narxlar)            #min() eng kichigini chiqarib beradi.
# qimmat = max(narxlar)           #max() eng kattasini chiqarib beradi.
# barchasi = sum(narxlar)         #sum() barchasini yig'indisini chiqarib beradi.
# print("Eng arzon narx: ", arzon)
# print("eng qimmat narx: ", qimmat)
# print("jami summa: ", barchasi)

# phone = ['iphone 13 pro', 'samsung A52S','samsung A10', 'samsung J2 core','redmi note 11','mi 9']
# my_phone = phone[1:4]             #ro'yxatni kesish
# print(my_phone)

# sonlar  = [1,13, 34, 45,67]
# sonlar1 = sonlar[:]          #ro'yxatdn  nusxa olish
# sonlar1.append(78)
# sonlar1.append(80)
# print(sonlar)
# print(sonlar1)

# ismlar = ("Habibullo", "Azizbek", "Samandar","Bobur")
# ismlar = list(ismlar)
# ismlar.append("Xayrullo")
# ismlar.remove("Bobur")
# ismlar[2]="Doniyor"
# ismlar = tuple(ismlar)
# print(ismlar)

            #HOMEWORK
# 1. O'zingizga yoqgan moshinalarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring.
moshina = ["mersedes benz","bugatti","ferrari","malibu","tesla","cobalt","takuma"]
moshina.sort()
print("1-misol: ",moshina, "\n")

# 2. Yozgan ro'yxatingizning uzunligini konsolga chiqaring.
moshina = ["mersedes benz","bugatti","ferrari","malibu","tesla","cobalt","takuma"]
print("2-misol: ", " Ro'yxatdagi moshinalar soni: ", len(moshina), "\n")

# 3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring.
moshina = ["mesedes benz","bugatti","ferrari","malibu","tesla","cobalt","takuma"]
print("3- misol: ", "Ro'yxatning tartiblangan elementlari: ", sorted(moshina))
print("\n")

#4.  sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring.
moshina = ["mersedes benz","bugatti","ferrari","malibu","tesla","cobalt","takuma"]
print("4-misol: ", "Ro'yxatni teskari tartibi: ", sorted(moshina, reverse = True), "\n")

# 5. Asl ro'yxatni qaytadan konsolga chiqaring.
moshina = ["mersedes benz","bugatti","ferrari","malibu","tesla","cobalt","takuma"]
print("5-misol: ", sorted(moshina, reverse = True))
print("Asl ro'yxat: ", moshina, "\n")

# 6.  reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring.
fasl = ["yoz","qish","bahor","kuz"]
fasl.reverse()
print("6-misol: ", "Ro'yxatni ortidan boshlab chiqarish: ", fasl)
print("\n")

# 7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
colours = ["red","blue","white","black","yellow","orange"]
colours.sort()
print("7-misol: ", "alifbo tartibida: ", colours)
colours.sort(reverse = True)
print("alifboga teskari tartib: ", colours)
print("\n")

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
juft_sonlar = list(range(120,1200,2))
print("8-misol: ", "Juft sonlar: ", juft_sonlar)
print("\n")

# • Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring.
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)
yigindi = sum(juft_sonlar)
print("9-misol: ", "max = ", eng_katta)
print("min = ", eng_kichik)
print("sum = ", yigindi)
print("\n")
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va
# konsolga chiqaring
print("10-misol: ", "ayirma = ", eng_katta - eng_kichik)
print("\n")
#  Ro'yxatdagi elementlar sonini hisoblang
print("11-misol: ", "elementlar soni: ", len(juft_sonlar))
print("\n")
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
son = juft_sonlar[0:20]
print("12-misol: ", "boshidan: ", son)
son1 = juft_sonlar[260:280]
print("o'rtasidan: ", son1)
son2 = juft_sonlar[520:540]
print("oxiridan: ", son2)
print("\n")
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["osh","sho'rva","norin","kabob","mastava"]
print("13-misol: ", taomlar)
print("\n")
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[1:4]
print("14-misol: ", nonushta)
print("\n")
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va
# qo'shimcha 2 ta taom qo'shing
nonushta.remove("norin")
nonushta.append("chuchvara")
nonushta.append("jarkob")
print("15-misol:  ",nonushta)
print("\n")
#  Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print("16-misol: ", taomlar)
print(nonushta)
print("\n")
#  Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.# nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = ("sho'rva","kabob","chuchvara","jarkob")
print("17-misol: ", nonushta)
nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)
print("\n")