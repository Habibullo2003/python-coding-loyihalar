# # taklifnoma = ['Rustam', 'Muzaffar', 'Alisher','Dilmurod','Sherzod']
# # for  mehmon in taklifnoma:
# #     print("Assalomu alaykum",mehmon)
# #     print("Dars tugadi!")

# son = list(range(7))
# for  chiqar  in  son:
#     print(chiqar)

# sonlar = list(range(11))
# sonlar_kv = []
# for son in sonlar:
#     sonlar_kv.append(son**2)

# print(sonlar)
# print(sonlar_kv)

# print("5 ta kelmagan bollarni ismini kiriting:")
# dostlar = []
# for ism in range(6):
#     dostlar.append(input(f"{ism+1} - darsga kelmagan bolani ismini yozing>>>"))

# print("Kelmagan bollar ro'yxati:",dostlar)

# davlatlar = ['GERMANIYA','UZB','KANADA','ROSSIYA','UKRAINA']
# for davlat in davlatlar:
#     if davlat == 'UZB':
#         print(davlat.lower())
#     else:
#         print(davlat)
# print(davlatlar)
       #Homework
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga u 
#odam haqida qisqacha izoh yozib xabar yozing.
ismlar = ['Anvar','Azam','Ahror','Azizbek','Abduqodir']
for xabar in ismlar:
    print("Assalomu alaykum ", xabar, "yaxshimisan!")
print("nega kecha darsga kelmading?😥😥😥",ismlar[0])
print("Uyga vazifani bajardingmi?😠😠😠",ismlar[1])
print("Uyga vazifani nega bajarmading?🤔🤔🤔",ismlar[2])
print("Daftaringni olib kel!😡😡😡",ismlar[3])
print("bu vazifani xato bajaribsan!🙄🙄🙄",ismlar[4])

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni
#chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
ismlar = ['Anvar','Azam','Ahror','Azizbek','Abduqodir']
for xabar in ismlar:
    print("Assalomu alaykum ", xabar, "yaxshimisan!")
print(f"ekranga {len(ismlar)} marta takrorlanadi.")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining
#kubini toq sonlar kubi deb yangi qatordan konsolga chiqaring.
son = list(range(10,100))
for sonlar in son:
    print(sonlar)
    print(f"toq sonlar kubi: {sonlar**3}")

# Foydalanuvchidan 10 ta eng sevimli kitoblarini kiritshni so'rang, va Kitoblar degan
#ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kitoblar = []
print("10 ta eng sevimli kitobingizni kiriting: ")
for n in range(11):
    kitoblar.append(input(f"{n+1} - kitobni kiriting: "))
print(list(kitoblar))

#Foydalanuvchidan bugun nechta kitob o’qiganini so'rang, va har bir o’qigan kitobini
#nomini birma-bir so'rab ro'yxatga yozib. Siz oq’igan kitoblar deb Ro'yxatni konsolga 
#chiqaring.
kitoblar = []
print(input("bugun nechta kitob o'qidingiz: "))
for n in range(1,3):
    kitoblar.append(input(f"{n} - o'qigan kitobingizni kiriting: "))
print("siz o'qigan kitoblar: ", list(kitoblar))