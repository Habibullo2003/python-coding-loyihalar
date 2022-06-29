import random as r
   #tasodifiy sonlarni chiqarish kutubxonasi

# son = r.randint(20,100)  
# print(son)                   # #tasodifiy sonlar chiqazib beradi.

# mevalar = ['anor','olma','olxo\'ri','gilos','nok','o\'rik','banan']
# print(mevalar)

# meva = r.choice(mevalar)
# print(meva)

# print(r.choice(meva))

# 3- kod. bu kodda range yordamida 1 dan 100 gacha bo'lgan sonlardan tashkil topgan sonlar degan o'zgaruvchi bilan 
# belgilab list yaratamiz. print orqali ekranga natija chiqarsak, bizga list qavsi ichida 1 dan 100 gacha bo'lgan sonlar
#chiqib keladi. print(r.choice(sonlar)) qilib biz tasodifiy bitta sonni tanlab olamiz.

# sonlar = list(range(1,100))
# print(sonlar)

# print(r.choice(sonlar))

# sonlar = list(range(1,10))
# print(sonlar)

# r.shuffle(sonlar)  # shuffle metodi list ichidagi sonlar ketma-ketligini aralashtirib tashlaydi.
# print(sonlar)


print("""
     Kompyuter bilan son topish o'yini 
     Salom, men 1, dan 20 - gacha son o'yladim topaolasizmi?
         """)
kompyuter_son = r.randint(1,20)
n = 0
user1 = ' '
while True:
    user = int(input("Son kiriting>>>")) 
    n += 1

    if user == kompyuter_son:
        print(f"Tabriklaymiz siz {n} - urinishda topdingiz ")
        n = 0
        kompyuter_son = r.randint(1,20)
        user1 = input("Yana o'yin o'ynaymizmi? 'ha' yoki 'yoq' ni tanlang:")

    elif user > kompyuter_son:
        print(f"Xato men o'ylagan son {user} dan kichik")

    elif user < kompyuter_son:
        print(f"Xato men o'ylagan son {user} dan katta")
        
    if user1 == 'ha':
        continue
    elif user1 == 'yoq':
        print("O'yin tugadi! Xayr")
        break 


