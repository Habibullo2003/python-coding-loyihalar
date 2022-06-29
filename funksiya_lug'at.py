# def my_func(ism,familiya,yoshi = 25):
#     """ Bu funksiya ismni to'liq chiqarib beradi """
#     full_name = f" {ism} {familiya} {yoshi} "
#     return full_name

# print(my_func.__doc__)

# name1 = my_func(familiya = "Azimov",ism = "Ulug'bek")
# print(name1)

# def moshinalar(nomi,rangi,narxi,yili,karobkasi = ' '):
#     """ Bu funksiya moshinalar haqida ma'lumot chiqarib beradi """

#     if moshinalar:
#         moshina = f" {nomi} {rangi} {narxi} {yili} {karobkasi} "
#     else:
#         moshina = f" {nomi} {rangi} {narxi} {yili} "

#     return moshina

# print(moshinalar.__doc__)

# moshina1 = moshinalar("Ravon","qora",40000,2019,"avto")
# moshina2 = moshinalar("malibu","oq",60000,2021)

# print(f"Karobkasi ma'lum: {moshina1}")
# print(f"Karobkasi noma'lum: {moshina2}")


# def telefonlar(kompaniya,model,rangi,narxi,operativka,yili = None):
#     """ Bu funksiya moshinalar haqida ma'lumot chiqarib beradi """
#     telefon = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rangi' : rangi,
#         'narxi' : narxi,
#         'operativka' : operativka,
#         'yili' : yili
#     }
#     return telefon

# telefon1 = telefonlar("apple", "Iphone12","qora",800,2020,128)
# telefon2 = telefonlar("samsung", "Galaxy A52S","kulrang",400,2022)

# print(telefon1)
# print(telefon2)

          #homework

# Userdan ismi, familiyasi, tug'ilgan_yili, yoshi, tug'ilgan joyi, yashash manzili, telefon raqamini
#olib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Ba'zi argumentlarni kiritishni ixtiyoriy
#yoki standart qiymat bilan bering (Misol uchun: familya, yashash-manzili)

# def user(ismi,familiyasi,t_yili,t_joyi,yashash_manzili,yoshi=19,telefon_raqami=943352527,):
#     """ Bu funksiya foydalanuvchidan ma'lumot olib uni consolga chiqarib beradi """
#     users = {
#         'ismi' : ismi,
#         'familiyasi' : familiyasi,
#         'tug\'ilgan yili' : t_yili,
#         'tug\'ilgan joyi' : t_joyi,
#         'yoshi' : yoshi,
#         'telefon raqami' : telefon_raqami
#     }
#     return users

# users1 = user("Habibullo","Xayrullayev",2003,"Qashqadaryo viloyati","Jeynov shaharchasi")
# users2 = user("Bobur","Davlatboyev",2003,"Xorazm viloyati","Do'simbiy shaharchasi", telefon_raqami=939020320)
# users3 = user("Nodirbek","Mamasoliyev",2004,"Namangan viloyati","To'raqo'rg'on tumani", telefon_raqami=940395019)

# print(f"{users1} '\n', {users2} '\n', {users3}")

# 2-qism huddi shu misolni while ko’rinishida foydalanuvchidan qayta qayta so’raydigan funksiya yozing.

# def user(ismi,familiyasi,t_yili,t_joyi,yashash_manzili,yoshi=19,telefon_raqami=943352527,):
#     """ Bu funksiya foydalanuvchidan ma'lumot olib uni consolga chiqarib beradi """
#     while True:
#         ismi = input("Ismni kiriting: ")
#         familiyasi = input("Familiyasini kiriting: ")
#         t_yili = int(input("Tug'ilgan yilingizni kiriting: "))
#         t_joyi = input("Tug'ilgan joyingizni kiriting: ")
#         yashash_manzili = input("Yashash manzilini kiriting: ")
#         users = {
#             'ismi' : ismi,
#             'familiyasi' : familiyasi,
#             'tug\'ilgan yili' : t_yili,
#             'tug\'ilgan joyi' : t_joyi,
#             'yoshi' : yoshi,
#             'telefon raqami': telefon_raqami
#         }
#         print(users)
#         break

# user('ismi','familiyasi','t_yili','t_joyi','yashash_manzili',yoshi=19,telefon_raqami=943352527,)

# Ikkita son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing.
def son(a,b):
    """ Bu funksiya userdan 2 ta son olib kattasini consolga chiqarib beradi  """
    while True:
        if a > b:
            son = a
        else:
            son = b
        return son
sonlar = son(9,8)
print(sonlar)