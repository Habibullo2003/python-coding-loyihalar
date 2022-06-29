# def salom_ber():
#     print("Assalomu alaykum")

# salom_ber()

# def my_func(name):
#     """ Bu funksiyamiz ism qabul qilib unga salom beradi """
#     print(f"Salom hurmatli {name}")

# my_func("Habibullo")

# print(my_func.__doc__)

# def talaba(ismi, yoshi, fakulteti, kursi):
#      """ Bu funksiyamiz parametrga qiymat berib argumentga yuklaydi"""
#      print(f"Assalomu alaykum mening ismim {ismi.title()}, yoshim - {yoshi} da, {fakulteti} fakulteti, {kursi}- kurs talabasiman")

# print(talaba.__doc__)
# talaba("habibullo", 19, "Kompyuter injineringi", 1)    


     #Homework
# Userdan ikkita son oling va, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar 
# sonlar ikkisi teng bo'lsa “ siz kiritgan sonlar teng! " degan xabarni chiqsin.
# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))
# def my_func(a,b):
#      """ Bu funksiya o'ziga 2 ta a va b o'zgaruvchilarni qabul qilib oladi va bizga kattasini chiqarib beradi  """
#      if a > b:
#           print(a)
#      elif a < b:
#           print(b)
#      else:
#           print("siz kiriting sonlar teng.")

# print(my_func.__doc__)
# my_func(a,b)

# User’dan ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# def user(ism,yosh,h_yil = 2022):

#      """ Bu funksiya userdan ism va yoshni so'rab uni tug'ilgan yilini chiqarib beradi """
#      print(f""" 
#                 Ismi - {ism}. 
#                 Yoshi - {yosh}.
#                 tug'ilgan yili - {h_yil - yosh}
#      """)

# print(user.__doc__)
# user("Habibullo", 19)


# User’dan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# a = int(input("a = "))
# def son(a):
#      """ Bu funksiya userdan son olib uning kvadrati va kubini konsolga chiqarib beradi.  """
#      print(f"""
#       {a} sonining kvadrati {a**2} ga teng 
#       {a} soninig kubi {a**3} ga teng  
#         """)
 
# print(son.__doc__)
# son(a)

# User’dan son oling va, son juft yoki toqligini aniqlab konsolga chiqaruvchi funksiya yozing.

# a = int(input(" a sonini kiriting: "))

# def son(a):

#      """ Bu funksiya userdan son oib uning juft yoki toqligini ekranga chiqarib beradi. """

#      if a % 2 == 0:
#           print(f" {a} - soni juft ")
#      else:
#           print(f" {a} - soni toq")

# print(son.__doc__)
# son(a)

# User’dan son olib, sonni 2-dan 20-gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.

# a = int(input(" a sonini kiriting: "))
# def bulish(a):
#      while True:
#           for i in range(2,20):
#                if a % i == 0:
#                     print(f"{a} ni qoldiqli bo'lganda {i} ga {a % i} qoldiq qoladi")
#                else:
#                     print(f"{a} soni {i} ga qoldiqli bo'linmaydi.")
#           break

# bulish(a)