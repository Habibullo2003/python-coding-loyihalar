# son = 1
# while son<=10:
#     print(son, end = ' , ')    # end   vertikal holatda chiqarib beradi.
#     son += 1
# print ("Dastur tugadi!")

# print("Kiritilgan sonning kvadratini chiqaruvchi dastur:")
# savol = "Istalgan son kiriting. Dasturni to'xtatish uchun 'stop' buyrug'ini yozing: "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print("Dastur yakunlandi.")

# print("Kiritilgan sonningkubini hisoblovchi dastur: ")
# a = input(" a sonni kiriting: ")
# a += ("dasturni to'xtatish uchun 'exit' tugmasini bosing: ")
# while True:
#     qiymat = input(a)
#     if qiymat != 'to\'xta':
#         break
#     else:
#         print(float(qiymat)**3)
#         print("dastur yakunlandi!")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati = {son**2} ga teng")

# t_sonlar = list(range(1,21,2))
# j_sonlar = list(range(0,20,2))
# for son in t_sonlar:
#     if son == 21:
#         continue
#     print(f"{son} ning kvadrati = {son**2} ga teng.")
# for son in j_sonlar:
#     if son == 20:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.") 

# son = 0
# while son < 30:
#     son += 1
#     if son % 2 == 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son < 0:
#     son += 1
#     if son % 2 != 0:  ABADIY TSIKL.
#         continue
#     else:
#         print(son)

#Foydalanuvchidan yaxshi ko'rgan kinolarini kiritishni so'rang. Va foydalanuvchi stop so'zini
#yozishi bilan dasturni to’xtasin!
kino = input("yaxshi ko'rgan kinolaringizni kiriting: ")
while kino != 'stop':
        print(kino)
    
        print("dastur yakunlandi!")