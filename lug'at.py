# ismlar = {}
# print(ismlar)

# ismlar['ism'] = 'Habibullo'
# ismlar['yoshi'] = 19
# ismlar['kursi'] = 1
# ismlar['fakulteti'] = "K.I.F"
# print(ismlar)

# talaba = {'ismi':'qobil','familiya':'karimov','t_yili':1996,'viloyati':'samarqand'}
# print(talaba)
# del talaba['viloyati']
# print(talaba)

# talaba = {'ismi':'qobil','familiya':'karimov','t_yili':1996,'viloyati':'samarqand'}
# print(talaba)

# talaba['ismi'] = "Habibullo"
# talaba['familiya'] = "Xayrullayev"
# talaba['t_yili'] = 2003
# talaba['viloyati'] = 'Qashqadaryo'
# print(talaba)

# del talaba['t_yili']  # del funksiyasi qiymat o'chirib beradi.
# print(talaba)

# taklifnoma = {
#     'nahorgi osh' : "25 - mayda",
#     'to\'y' : '1-iyunda', 
#     'sunnat to\'y' : '7-iyunda'
# }
# print(taklifnoma)

# moshinalar = {
#     'Anvar' : 'captiva',
#     'Zuhriddin' : 'tesla',
#     'Bobur' : 'matiz',
#     'Zaynobiddin' : 'mers'
# }
# moshina = moshinalar['Bobur']
# print('Boburning moshinnasi ',moshina)

# moshina = moshinalar.get('Doston','Bzda bunday ism mavjud emas')
# print(moshina)

#Homework

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
#kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi
#ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, 
#Samarqand viloyatida tug'ilgan

# otam   =  {
# "ismi" :"Ro'zimurod",
# "tugilgan yili" :"1981 - yil",
# "shahri" : "Jeynov",
# "manzili" : "Jeynov mahallasi" }
# print(f"Otamning ismi {otam['ismi']} {otam['tugilgan yili']} {otam['shahri']} shahri {otam['manzili']}da tug'ilgan ")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi
#bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
otam = {'taom' : 'osh'}
# onam = {'taom' : 'manti'}
# uzim = {'taom' : 'qovurilgan kartoshka'}
# katta_ukam = {'taom' : "kabob"}
# kichik_ukam = {'taom' : "chuchvara"}
# print( f""" 
#         Otamning sevimli taomi {otam['taom']}
#         Onamning sevimli taomi {onam['taom']}
#         O'zimning sevimli taomim {uzim['taom']} 
#         Katta ukamning sevimli taomi {katta_ukam['taom']}
#         Kichkina ukamning sevimli taomi {kichik_ukam['taom']}
#         """)

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
#(masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# phyton = {'integer' :'butun sonlar','float':'haqiqiy sonlar','string':'satr','if':'agar','else':'aks holda'}
# print("PHYTON izohli lug'ati\n")
# print(f"""
#   integer - {phyton['integer']}
#   float   - {phyton['float']}
#   string  - {phyton['string']}
#   if - {phyton['if']}
#   else - {phyton['else']}
# """)

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib
#bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
phyton = {'integer' :'butun sonlar','float':'haqiqiy sonlar','string':'satr','if':'agar','else':'aks holda'}
lugat = input("So'z kiriting: ")
lugat = lugat
if lugat.lower() in phyton:
    lugat = phyton['integer']
    lugat = phyton['float']
    lugat = phyton['string']
    lugat = phyton['if']
    lugat = phyton['else']
    print("siz kiritgan so'z lug'atimizda mavjud")
    print(lugat)
else:
    print("Bunday so'z mavjud emas")
