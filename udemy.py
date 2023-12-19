#name = input("name: ")
#age = int(input("age : "))
#age = age -1
#print("your name is : " +name)
#print("you are " +str(age)+ " years old")

#name = "cansu kayalar"
#print(len(name))
#print(name[0:end:2])
#print(name[::-1])


#name=input("name: ")
#name = name*3
#print(name)
#print("your name is : " +name)
#surname= name + "kayalar"
#print(surname)


#import time
#for i in range(10,0,-1):
#    print(i)
#    time.sleep(1)
#print("happy new year")

#meyveler = ["elma" , "armut" , "muz"]
#sebzeler = ["biber" , "domates"]
#for i in meyveler:
#    for j in sebzeler:
#       print(i,j)

#while True:
 #   age = int(input("age : "))
 #   if age == 20:
 #       break
 #   elif 20%age==0:
 #       break

#number= "123-465-78"
#for i in number:
#    if i == "":
#        continue
#    print(i,end="9")


#for i in range(1,20):
#    if i== 13 :
#        pass
#    else:
#        print(i+1)


#sembol = input("sembol : ")
#for i in sembol :
#    print(i*3)

#kolon= int(input("kolon : "))
#satir= int(input("satır: "))
#sembol =input("sembol : ")

#for i in range(kolon) :
#    for j in range(satir) :
#        print(sembol,end="-")
#   print()

#cansu ="cansu"
#for i in cansu:
#    print(i*len(cansu))

#k= 0
#j= 0
#for i in range (1,5, 1):
#    for j in range(2,4):
#        for k in range(3,6):
#          print(i * '*')
#    print(j * '-')
#    print(k * '+')

#isim = input("isim: ")
#soyad = input("soyad: ")

#print("ur name is {} and ur surname is {}" .format(isim,soyad))


#import time
#liste= ["a" , "b" , "c" ,1, 2, 3]
#num= 12345678
#j = 0
#print(liste[2])
#for i in range(0,num,10):
#    for j in range(0,liste[5]):
#     print(i)
#    print(j)
#    time.sleep(1)

#food = ["a", "b","c"]
#food.append("x")
#food.remove("a")
#food.insert(0,"k")
#food.pop()
#food.sort()
#print(food)

#cansu = (166 , "kayalar" , "girl" ,166)
#print(cansu.count(166))
#print(cansu.index(166))
#for x in cansu:
#    print(x)
#if "kayalar" in cansu:
#    print("cansu is here.") #tuple

#mail = ""
#password = ""
#while mail=="":
#    mail= input("mail adresi :")
#    if mail != "cansu.com" :
#       print("hatalı giriş.")
#    else :
#        print("şifre girin")
#        while password=="":
#            password = input("şifre :")
#        if password!= "1234":
#            print("hatalı şifre. Tekrar dene.")

#import time
#liste=["a" , "b","c","d"]
#tuple = [1,2,3,4,5,6,7]
#for i in tuple:
#    for j in liste:
#        print(i,j)
#        time.sleep(1)

#import time
#text = "seni seviyorum"
#for i in text[0:]:
#    print(i)
#    time.sleep(0.7)
#for i in range(1,10):
#    print(i * ' <3')

#animals = {'sürüngen' : 'timsah ' ,
#           'omurgasız' : 'denizanası' }
#print(animals['omurgasız'])
#print(animals.keys())
#animals.update({'kuş':'karga'})
#for key,value in animals.items() :
#    print(key,value)

#name="Cansu Kayalar"
#if (name[7]).islower():
#    print(name[0]+str(name[6])+" online")
#    name = name.capitalize()
#for i in name:
#    print(i +str("*"))
#first_name = name[0:].upper()
#print(first_name)

#def hello(name,surname,age,number):
#    print("hello " +name,surname)
#    print("we will call u with " +str(number))
#    print("you re " +str(age)+ " years old")
##hello("cansu" , "kayalar" , 20 , 1234)
#i= input("may name is : " )
#j= input("surname:")
#u= input("age : ")
#p= input("number : ")
#hello(i,j,u,p)

#def topla(num1,num2):
#    return num1+ num2
#print(topla(783,90))

#def sent(first,middle,last):
#    print(first,middle,last)
#sent(middle="ben"  , last= "cansu",first= "merhaba" )

#animal=input("hayvan :")
#yemek= input("yemek:")
#print("genelde {0} yemekleri şudur : {0} " .format(animal,yemek))
'''
import random
#x= random.randint(1,100)
#y= random.random()
liste= ["taş" , "kağıt", "makas"]
z=random.choice(liste)

k=input("taş kağıt makas ? : ")
b= print(z)
if b=="taş" and k=="kağıt" :
    print("kağıt taşı sardı. kullanıcı kazandı!")
elif b== "taş" and k==" makas" :
    print("taş makası ezdi , bilgisayar kazandı!")
elif b== "kağıt" and k==" makas" :
    print("makas kağıdı kesti,kullanıcı kazandı !")
elif b == "kağıt" and k == " taş":
    print("kağıt taşı sardı,bilgisayar kazandı!")
elif b == "makas" and k == " taş":
    print("taş makası ezdi ,kullanıcı kazandı!")
elif b == "makas" and k == "kağıt":
    print("makas kağıdı kesti , bilgisayar kazandı!")
else :
    print("berabere")
'''
'''
import random
x= random.randint(1,100)
liste =["taş" , "kağıt", "makas"]
z=random.choice(liste)
cards = [1,2,3,4,5,6,7,8,9,"Q","J","K","A"]
random.shuffle(cards)
print(cards)
'''
'''
import random
x = random.randint(1,100)
y = int(input("aklından bi sayı tut:" ))
while x != y:
    if x < y:
        y = int(input("daha küçük bi sayı : "))
    elif x > y:
        y = int(input("daha büyük bi sayı : "))

print("TEBRİKLERRR! DOĞRU BİLDİNİZ AQ")
'''
'''
import random
x= random.randint(1,100)
y=int(input("bir sayı tut: "))
while x!=y :
    if x<y :
        y = int(input("daha küçük bi sayı tut :"))
    elif x>y :
        y= int(input("daha büyük bir sayı tut :"))
print("TEBRİKLER BULDUN!")
'''
'''
import random
#x= random.randint(1,100)
#y= random.random()
liste= ["taş" , "kağıt", "makas"]
z=random.choice(liste)

k=input("taş kağıt makas ? : ")
if z == "taş" and k == "kağıt":
    print("kağıt taşı sardı. kullanıcı kazandı!")
elif z == "taş" and k == "makas":
    print("taş makası ezdi , bilgisayar kazandı!")
elif z == "kağıt" and k == "makas":
    print("makas kağıdı kesti,kullanıcı kazandı !")
elif z == "kağıt" and k == "taş":
    print("kağıt taşı sardı,bilgisayar kazandı!")
elif z == "makas" and k == "taş":
    print("taş makası ezdi ,kullanıcı kazandı!")
elif z == "makas" and k == "kağıt":
    print("makas kağıdı kesti , bilgisayar kazandı!")
else :
    print(z)
    print("berabere")
'''
'''
rte=meralmommy=ince=kk=imamoglu=0
print("oy kullanma platformuna hoşgeldiniz")
members= ["rte" , "meralmommy" , "ince" , "kk" , "imamoğlu"]
age=int(input("yaşınızı giriniz : "))
while age>=18 :
'''
'''
import time
import random
members= ["rte" , "meralmommy" , "ince" , "kk" , "imamoğlu"]
x= random.choice(members)
for i in range(4,0,-1):
    print(i)
    time.sleep(0.8)
print(x)
'''
'''girls=["eda","ela","elanur","cansu","ayşe","sevgi","eylül","merve"]
boys=["taha","gürkan","sefa","mehmet"]
for i in girls:
    for j in boys:
        print(i,j)
print(len(i,j))'''

'''print("isim şehir hayvan bitki oyununa hoşgeldiniz!")
import random
harfler = "abcçdefghıijklmnoöprsştuüvyz"
x=random.choice(harfler)
print(x)
def oyun(isim,sehir,hayvan,bitki):
 cevapp=input(oyun(isim={} , sehir={} , hayvan={} , bitki={} ))
isim= input("isim :")
sehir=input("şehir : ")
hayvan= input("hayvan : ")
bitki =input("bitki: ")
cevap= [isim,sehir,hayvan,bitki]
if cevap[0][0] or cevap[1][0] or cevap[2][0] or cevap[3][0] !=x:
    print("yanlış harfle başladınız.")
else :
    print("nice!")
'''
'''import time
print("GERİ SAYIM BAŞLATILIYOR...")
for i in range(10,0,-1):
    print("SON {} SANİYE.".format(i))
    time.sleep(1)
print("kıyamet başlıyor!")'''

'''import random
print("AŞK UYUMU TESTİ")
name1= input("1. isim :")
name2=input("2. isim : ")
x=random.randint(0,100)
print("uyumunuz : %{}".format(x))
'''
'''import random #sayı tahmin et. sayı doğru yeri yanlış vs desin..> eğer girdğin sayı pc dekkine eşit değilse ve x sayısının içindekileri sayıların konumlarını y sayısıyla karşılatır
x= str(random.randint(100,500))
print(x)
y= str(input("tahmin : "))
while x != y:
    if y[0] == x[0] or y[1] == x[1] or y[2] == x[2]:
        print("sayı ve yeri doğru")
    else:
        print("yanlış")'''

'''try:
    bolunen=int(input("bölünen sayı : "))
    bolen = int (input("bölen sayı : "))
    result = bolunen/bolen
    print(result)
except ZeroDivisionError:
    print("sayı sıfıra bölünemez.")
except ValueError:
    print("sayı ancak sayıya bölünebilir.")
#except Exception:
#    print("bir şeyler yanlış gitti.")'''

'''import random #sayı tahmin et. sayı doğru yeri yanlış vs desin..> eğer girdğin sayı pc dekkine eşit değilse ve x sayısının içindekileri sayıların konumlarını y sayısıyla karşılatır
x = str(random.randint(100, 5000))
print(x)
y = str(input("tahmin : "))
while x != y:
    for i in range(0, len(x), 1):
        if y[i] != x[i]:
            print(f"{i + 1} . sayı yanlış")
    y = str(input("tahmin : "))
'''
'''print("çayı kim demleyecek????")
names =["eda","ela","elanur","cansu","ayşe","sevgi","eylül","merve","taha","gürkan","sefa","mehmet"]
x=random.choice(names)
print(x)'''
'''print("asal sayı bulma")
y=int(input("kaça kadar olan asal sayılar? : "))
for i in range(1,y):
    if i >1 :
        if y % i == 0:
            print(i)
'''

'''try :
    num1 = int(input("sayı : "))
    num2=int(input("sayı : "))
    toplam = num1+num2
    print(toplam)
except Exception:
    print("bir şeyler ters gitti") '''

'''import os

path = "C:\\Users\\Cansu KAYALAR\\Desktop\\test.txt"
if os.path.exists(path):
    print("dosya mevcut")
    if os.path.isfile(path):
        print("true location")
    else: os.path.isdir(path)
    print("bu bir klasör")
else:
    print("bu dosya yok")'''

'''import os
path = "C:\\Users\\Cansu KAYALAR\\Desktop\\test2.txt"
if os.path.exists(path):
    print("bu dosya mevcut")
    if os.path.isfile(path):
        print("bu bir dosyadır")

else :
    print("bu dosya mevcut değil. ")'''
'''try:
    with open("C:\\Users\\Cansu KAYALAR\\Desktop\\klasor\\klasor.txt.txt") as file:
        print(file.read())
except Exception:
    print("dosya bulunamadı")'''

'''text = "heyyyyyyy\nbu bir deneme metnidir\nkapis\n"
with open('test2','w') as file:
    file.write(text)'''

'''import shutil
shutil.copy('test2','copy.txt')'''

'''import os
source = "klasor"
destination = "C:\\Users\\Cansu KAYALAR\\Desktop\\klasor"
try:
    if os.path.exists(destination):
        print("dosya zaten var")
    else:
        os.replace(source,destination)
        print(source+"dosya taşındı")
except FileNotFoundError:
    print(source+"dosya bulunamadı")'''

'''import os
try:
    #os.remove('folder')
    os.rmdir('folder')
    print("dosya silindi")
except FileNotFoundError:
    print("dosya zaten silindi.")
except PermissionError:
    print("dosya değiştirme izniniz yok.")
'''
import random #sayı tahmin et. sayı doğru yeri yanlış vs desin..> eğer girdğin sayı pc dekkine eşit değilse ve x sayısının içindekileri sayıların konumlarını y sayısıyla karşılatır
x = str(random.randint(100, 500))
y = str(input("tahmin : "))
while x != y:
    for i in range(0, len(x), 1):
        if y[i] != x[i]:
            print(f"{i + 1} . sayı yanlış")
    y = str(input("tahmin : "))

