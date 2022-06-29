# dostlar = []
# print("Do'stlaringiz ro'yxatini tuzamiz:")
# k = 1
# while True:
#     savol = f"Do'stlaringiz ismini kiriting: "
#     dost = input(savol)
#     dostlar.append(dost)
#     javob = input("Yana do'stingiz ismini qo'shasizmi? ha/yo'q: ")
#     if javob == "ha":
#         k+=1
#         continue
#     else:
#         break
#     print("Do'stlaringiz ro'yxati:")
# for dost in dostlar:
#     print(dost.title())

# telefonlar = ['redmi','samsung','iphone','redmi','artel','redmi']
# while 'redmi' in telefonlar:
#     telefonlar.remove('redmi')
# print(telefonlar)

#  RO'YXATDAN RO'YXATGA ELEMENT’ni KO'CHIRISH
# avtolar = ['nexia','spark','matiz','cobalt','malibu','traccer']
# sotilgan_avtolar = {}
# while avtolar:
#     avto = avtolar.pop()
#     qiymat = input(f"{avto.title()} ning narxini kiriting: ")
#     sotilgan_avtolar[avto] = qiymat
# print(sotilgan_avtolar, qiymat)

avtolar = ['nexia','spark','matiz','cobalt','malibu','traccer']
sotilgan_avtolar = {}
for avto in avtolar:
    avto = input(f"{avto.title} ")