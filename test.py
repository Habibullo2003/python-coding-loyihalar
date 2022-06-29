print("""
Salom. Onlayn do'konimizga xush kelibsiz. 🤝🤝🤝
Bizning do'konimizdan sizni bir-biridan ajoyib
kompyuterlarni xarid qilishingiz mumkin. 💻💻💻
     """)
k_nomi = input("kompyuter nomini kiriting: ")
k_narx = int(input("kompyuter narxini kiriting: "))
u_narx = int(input("Pulingizni kiriting: "))

while True:
    if k_narx <= u_narx:
        son = int(input("""
        Xaridni amalga oshirish uchun 1 ni bosing: 
        Xaridni bekor qilish uchun 2 ni bosing. 
        """))
    else:   
        print("Kechirasiz, sizining pulingiz xaridni amalga oshirish uchun yetmas ekan!") 
        print(f"Sizga {k_narx - u_narx} $ pul yetmayapti.😥😥😥 ")
        break
        
    if son == 1:
        print("Muhtaram mijoz sizda yetarlicha pul bor ekan")
        print(f"""
        Tabriklaymiz sizning xaridingiz muvaffaqiyatli amalga oshirildi.
        Sizga {u_narx - k_narx} $ pulingiz qaytarib beriladi.🤠🤠🤠
        """)
    elif son == 2:
        print("Xaridingiz bekor qilindi sizga pulingiz qaytarib beriladi.")
    elif son != 1 and son != 2:
        print('Dastur xato. Dastur ishlashi uchun 1 yoki 2 ni bosing.😡😡😡 ') 

    input("""
    Hurmatli mijoz bizning xizmatlardan foydalanganingiz uchun sizga tashakkur.
    Onlayn do'konimiz sizga yoqgan bo'lsa, Bizga 👍 stikerini yuboring: 
    Agar onlayn do'konimiz sizga yoqmagan bo'lsa bizga 👎 stikerini yuboring: 
    """)
    print("Fikr bildirganingiz uchun tashakkur.")
    


    print("""
        DARTUR YARATUVCHISI: - XAYRULLAYEV HABIBULLO
        DASTURNI TEKSHIRDI:  - MURODOV MUZAFFAR
    """)
    print("Dastur 2022-yil 3-iyun kunida tuzildi")
    continue
