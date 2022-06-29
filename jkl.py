import random as r
print(''
      '\n')
print("Keling kompyuter bilan son top o'yinini o'ynaymiz!\n"
      "Siz 1, dan 20 gacha son o'ylaysiz kompyuter topadi!\n"
      "Siz 1, dan 20 gacha son o'ylab inter tugmasini bosing:\n"
      "Men topaman:\n")
n=0
oyin = ''
start =input("Tayyor bolsangiz interni bosing:\n")
print("Start:")

while True:
    n+=1
    komp_oylagan_son = r.randint(1,20)
    print(komp_oylagan_son)
    biz_oylagan_son = input("Biz o'ylagan son☝️:\n"
"To'g'ri topgan bo'lsa 't'\n"
"kopyuter o'ylagan sondan kichik bo'lsa: '-'\n"
"kompyuter o'ylagan sondan katta bolsa: '+'\n"
)
    if biz_oylagan_son == 't':
        print(f"Tabriklaymiz siz {n} marta urinishda topdingiz")
        n=0
        oyin = input("Yana o'ynaymizmi? 'ha' yoki 'yoq' ni tanlang:\n")
        if oyin == 'ha':
            continue
        elif oyin == 'yoq':
            print("O'yin tugadi, XAYR!")
            break
        
    if biz_oylagan_son == '-':
        continue
    elif biz_oylagan_son == '+':
        continue
    else:
        print("Xato boshqa belgi kiritingiz: Yana urinib koring!")