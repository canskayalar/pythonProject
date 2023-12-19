''''
def faktoriyel(n):
    if n==1 or n==0 :
        return 1
    else:
        return n* faktoriyel(n-1)
print(faktoriyel(7))
'''

'''
def toplam(liste):
    if len(liste)== 0:
        return 0 
    else:
        return liste[0] + toplam(liste[1:])
liste= [ 1,2,3,4,5 ]
print(toplam(liste))
'''

'''
def ebob(x,y):
    c=int(x%y)
    while x!=0 and y!=0 and x>y :
        if x%y==0:
            return y

    if x%y!=0 :
         return c


print(ebob(15,10))
'''
'''
def faktoriyel(n):
    if n==0 or n==1:
        return 1
    else:
        return n*faktoriyel(n-1)

print(faktoriyel(9))
'''
'''
def ebob(x,y):

    while x>0 and y>0 and x>y :
        if x%y==0 :
            return y
        elif x%y!=0 :
            return x%y
print(ebob(20,10))
'''

'''
def add(list):
    if len(list)==0 :
        return 0
    else:
        return list[0] + add(list[1:])
list=[1,2,3,4,5,6,7,8,9]
print(add(list))
'''
'''
sayi=int(input("sayı:"))

for i in range(1,sayi+1):
         if sayi%i==0:
             print(i)

'''
'''def Greetings():
    Count = 3
    while (Count > 0):
        print("Hello")
        Count = Count - 1
        '''




























