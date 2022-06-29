# Super class yoki Ota class
# class Phone:
#     def __init__(self,nomi,modeli,narxi,operativka,ch_yili):
#         self.nomi = nomi
#         self.model = modeli
#         self.narx = narxi
#         self.operativka = operativka
#         self.ch_yili = ch_yili

#     def get_info(self):
#         info = f"Nomi: {self.nomi}, Modeli: {self.model}, Narxi: {self.narx}"
#         info += f"Operativkasi: {self.operativka}, Ishlab chiqarilgan yili: {self.ch_yili} "
#         return info

# phone1 = Phone("Redmi","Mi",175,64,2020)
# phone2 = Phone("Samsung S10","Samsung",500,128,2021)
# print(phone1.get_info())
# print(phone2.get_info())

# # Voris class
# class New_Phone(Phone):
#     def __init__(self,nomi,modeli,narxi,operativka,ch_yili,rangi):
#         super().__init__(nomi,modeli,narxi,operativka,ch_yili)
#         self.rang = rangi

#     def get_info(self):
#         info = f"Nomi: {self.nomi}, Modeli: {self.model}, Narxi: {self.narx}"
#         info += f"Operativkasi: {self.operativka}, Ishlab chiqarilgan yili: {self.ch_yili}, Rangi: {self.rang} "
#         return info

# phone3 = New_Phone("Iphone","Apple",800,128,2022,"Qora")
# print(phone3.get_info())

class Mashina:
    def __init__(self,nomi,modeli,rangi,narxi,yil=0):
        self.nomi = nomi
        self.model = modeli
        self.rang = rangi
        self.narx = narxi
        self.__yil = yil

    def get__yil(self):
        return self.__yil

mashina1 = Mashina("KIA k5","KIA","Qora",500,2022)
print(mashina1.model)
print(mashina1.get__yil())