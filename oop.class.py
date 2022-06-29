# class Talaba:
#     def __init__(self,ismi,fam,yoshi):
#         self.name = ismi
#         self.surname = fam
#         self.age = yoshi

# talaba1 =Talaba("Ozodbek",fam="Xayrullayev",yoshi=15)
# talaba2 =Talaba("Anvar","Hasanov",29)

# print(talaba1.surname)
# print(talaba2.name)
# print(talaba1.age)

# class Telefon:
#     def __init__(self,nomi,rangi,xotirasi,yili):
#         self.name = nomi
#         self.colour = rangi
#         self.xotira = xotirasi
#         self.year = yili

# telefon1 = Telefon("Galaxy A52S","qora",128,2021)

# print(f"telefon nomi: {telefon1.name}\ntelefon rangi: {telefon1.colour}\ntelefon xotirasi: {telefon1.xotira}\ntelefon sotuvga chiqarilgan yili: {telefon1.year}")


# class Dasturchi:
#     def __init__(self,ismi,fam,yoshi,sohasi,fakulteti,kursi,guruhi):
#         self.ism = ismi
#         self.fam = fam
#         self.yosh = yoshi
#         self.sohasi = sohasi
#         self.fakultet = fakulteti
#         self.kurs = kursi
#         self.guruh = guruhi

#     def get_ism(self):
#         return self.ism

#     def get_fam(self):
#         return self.fam

#     def get_yosh(self):
#         return self.yosh

#     def get_sohasi(self):
#         return self.sohasi

#     def get_fakultet(self):
#         return self.fakultet

#     def get_kurs(self):
#         return self.kurs

#     def get_guruh(self):
#         return self.guruhi

#     def yangi_info(self):
#         print(f"""
#     \n\ndasturchi ismi:{self.ism}.\ndasturchi familiyasi:{self.fam}.\ndasturchi yoshi:{self.yosh}.
#     dasturchi sohasi:{self.sohasi}.\ndasturchi fakulteti:{self.fakultet}
#     dasturchining kursi:{self.kurs}.\ndastuchi guruhi:{self.guruh}
#         """)

# dastur1 = Dasturchi("Habibullo","Xayrullayev",19,"Backend","K.I",1,"217-21")
# dastur1.yangi_info()
  

# class Foydalanuvchi:
#     def __init__(self,ism,fam,yosh):
#         self.ism = ism
#         self.fam = fam
#         self.yosh = yosh

#     def bosh_func1():
#         pass

#     def bosh_func2():
#         pass

# foy1 = Foydalanuvchi("A'zam","Aliyev",23)
# print(foy1.bosh_func1())



               #Homework
# Web sahifa uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida
# odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, 
# email, va hokazo)
# class user:
#     def __init__(self,ism,f_ism,email):
#         self.ism = ism
#         self.f_ism = f_ism
#         self.email = email

# user1 = user("Habibullo","@hxcr7","xayrullayevhabibullo745@gmail.com")
# print(f"\n\tism: {user1.ism}, foydealanuvchi ismi: {user1.f_ism}, foydalanuvchi emaili: {user1.email}")

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
# class Taom:
#     def __init__(self,nomi,narxi,soni):
#         self.name = nomi
#         self.narx = narxi
#         self.son = soni

#     def yangi_taom(self):
#         print(f"taom nomi {self.name}, taom narxi {self.narx}, taom soni: {self.son} ")

# taom1 = Taom("osh",20000,2)
# taom2 = Taom("kabob",25000,1)
# taom3 = Taom("free",17000,3)

# taom1.yangi_taom()

# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan
# ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon
# Valiyev, email: alijon1994@gmail.com).

# class Metod:
#     def __init__(self,foydalanuchi,ismi,familiyasi,emaili,password):
#         self.foydalanuvchi = foydalanuchi
#         self.ism = ismi
#         self.familiya = familiyasi
#         self.email = emaili
#         self.password = password

#     def get_info(self):
#         print(f"Foydalanuvchi: {self.foydalanuvchi}, ismi: {self.ism}, familiyasi: {self.familiya}, emaili: {self.email}, kodi: {self.password}")

# metod1 = Metod("xayru20003","Habibullo","Xayrullayev","xayrullayevhabibullo745@gmail.com",77777777)
# metod2 = Metod("hxcr7","Hasan","Karimov","hasankarimov5@gmail.com",11111111)
# metod3 = Metod("asj342","Jasur","Hasanov","jasurhasano77@gmail.com",88888888)

# metod1.get_info()
# metod2.get_info()
# metod3.get_info()

# Texnika degan class yarating va uni ichida (Telefon, Moshina, Samalyot, Poezd) argumentlarini qabul
# qilsin va class ichida yangi get_info() yangi method orqali texnika klassiga yangi Raketa digan argument 
# qo’shib chaqiring.
class Texnika:
    def __init__(self,telefon,moshina,samolyot,poyezd):
        self.telefon = telefon
        self.moshina = moshina
        self.samolyot = samolyot
        self.poyezd = poyezd

    def get_info(self,raketa):
        self.raketa = raketa
        print(f"telefon {self.telefon}, moshina: {self.moshina}, samolyot: {self.samolyot}, poyezd: {self.poyezd}, raketa: {self.raketa}")

texnika1 = Texnika("Samsung A52S","malibu","dreamliner","afrosiyob","baamboozle")

texnika1.get_info()