s=str(input("Satr kiriting : ")) ; n=len(s)
while n%2!=0:
    s+=" " ; n+=1
arr=[]
for i in range(2):
    col = []
    for j in range(round(n/2)): col.append(0)
    arr.append(col)
k=0 ; i=0 ; l=0 ; j=0
for i in s:
    arr[k][l]=ord(i)-30 ; k+=1
    if k==2: 
        k=0 ; l+=1
print("Satr kodlari : ")
for i in range(2):
    for j in range(round(n/2)): 
        if len(str(arr[i][j]))==1 : print(arr[i][j],end="    ")
        elif len(str(arr[i][j]))==2 : print(arr[i][j],end="   ")
        elif len(str(arr[i][j]))==3 : print(arr[i][j],end="  ")
    print()
print("Matritsani kiriting : ")
mat=[]  
for i in range(2):
    col1 = []
    for j in range(2): col1.append(0)
    mat.append(col1)
for i in range(2):
    for j in range(2):
        print("[",i,",",j,"]=",end="")
        x=int(input()) ; mat[i][j]=x
deter=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
if deter==0 : 
    print("Kiritilgan matritsa determinanti 0 ga teng , axborotni dekodlab bolmaydi !") 
    print("Dasturni boshqatdan ishlating!") 
    end()
print("Kopaytiriladigan matritsa : ")
for i in range(2):
    for j in range(2):
        print(mat[i][j],end=" ")
    print()
natija=[]
for i in range(2):
    col2 = []
    for j in range(round(n/2)): col2.append(0)
    natija.append(col2)
i=0; j=0;
for i in range(2):
    for j in range(round(n/2)):
        natija[i][j]=0
        for k in range(2): natija[i][j]+=mat[i][k]*arr[k][j]
print("Natija : ")
for i in range(2):
    for j in range(round(n/2)): 
        if len(str(natija[i][j]))==1 : print(natija[i][j],end="    ")
        elif len(str(natija[i][j]))==2 : print(natija[i][j],end="   ")
        elif len(str(natija[i][j]))==3 : print(natija[i][j],end="  ")
    print()
print("\nDekodlash : \n")
mat1=[]
for i in range(2):
    col3 = []
    for j in range(2): col3.append(0)
    mat1.append(col3)
mat1[0][0]=mat[1][1]*round((1/deter),2) ; mat1[0][1]=-mat[0][1]*round((1/deter),2)
mat1[1][0]=-mat[1][0]*round((1/deter),2) ; mat1[1][1]=mat[0][0]*round((1/deter),2)
print("Teskari matritsa : ")
for i in range(2):
    for j in range(2):
        print(mat1[i][j],end="  ")
    print()
print("Dekodlangan matritsa : ")
natija1=[]
for i in range(2):
    col4 = []
    for j in range(round(n/2)): col4.append(0)
    natija1.append(col4)
for i in range(2):
    for j in range(round(n/2)):
        natija1[i][j]=0
        for k in range(2): natija1[i][j]+=round(mat1[i][k]*natija[k][j],2)
for i in range(2):
    for j in range(round(n/2)): 
        if len(str(natija1[i][j]))==3 : print(natija1[i][j],end="    ")
        elif len(str(natija1[i][j]))==4 : print(natija1[i][j],end="   ")
        elif len(str(natija1[i][j]))==5 : print(natija1[i][j],end="  ")
    print()