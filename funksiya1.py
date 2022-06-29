def talaba(ismi, familiyasi, yoshi, fakulteti, kursi):
    talabalar = f" {ismi}, {familiyasi}, {yoshi}, {fakulteti}, {kursi} "
    return talabalar
    
talaba1 = talaba("Azamat","Fayziyev",19,"Kompyuter injinering",1)
talaba2 = talaba("Alisher","Obidov",20,"Dasturiy injinering",2)

print(f" 1 - talaba ma'lumotlari: {talaba1} \n 2 - talaba ma'lumotlari: {talaba2} ")