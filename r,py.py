import random as r

print("Assalomu aleykum keling sonni top o'yinini o'ynaymiz!\n",
    "Salom men 1, dan 20-gacha son o'yladim topolasizmi? "
    )
komp_son = r.randint(1,20)
n=0
oyin=' '
while True:
    a = int(input("Son kiriting:"))
    n+=1
    if a==komp_son:
        print(f"Tabriklaymiz siz {n}-marta urinishda topdingiz")
        n=0
        komp_son = r.randint(1,20)
        oyin = input("Yana o'yin o'ynaymizmi? 'ha' yoki 'yoq' ni tanlang:")
    elif a>komp_son:
        print("Xato! Siz o'ylagan sondan men o'ylagan son kichik: Yana urinib ko'ring!")
    elif a<komp_son:
        print("Xato! Siz oylagan sondan, men o'ylagan son katta: Yana urinib ko'ring!")
    if oyin=='ha':
        continue
    elif oyin=='yoq':
        print("O'yin tugadi! Xayr")
        break