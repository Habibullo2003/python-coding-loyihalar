import random as h

print("Keling kompyuter bilan son top o'yinini o'ynaymiz!\n"
      "Siz 1, dan 20 gacha son o'ylaysiz kompyuter topadi!\n"
      "Siz 1, dan 20 gacha son o'ylab inter tugmasini bosing:\n"
      "Men topaman:\n")
kompyuter_son = h.randint(1,20)
k = 0
start = "Enter tugmasini bosing: "
print("Start:")
while True:
    print("""
           siz 1, dan 20 gacha son o'ylab enter tugmasini bosing men topaman
           biz 15 sonini o'ylaymiz va kompyuter konsolida enter tugmasini bosamiz o'yin ishga yushadi
    """)
    kompyuter_son = h.randint(1,20)
    print(kompyuter_son)
    
    biz_uylagan_son = int(input("Sonni kiriting>>>"))
    user = input("'t', '+', '-' belgilardan bittasini tanlang: ")
    k+=1
    
    if biz_uylagan_son == kompyuter_son:
        if user == 't':
            print(f"Tabriklaymiz siz {k} - urinishda topdingiz ")
        
    elif biz_uylagan_son < kompyuter_son:
        if user == '-':
            print(f"Xato men o'ylagan son {biz_uylagan_son} dan kichik")
        
    elif biz_uylagan_son > kompyuter_son:
        if user == '+':
            print(f"Xato men o'ylagan son {biz_uylagan_son} dan katta")
    continue

    