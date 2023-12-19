oyuncu1 = input("nick giriniz : ")
oyuncu2 = input("nick giriniz : ")

if  len(oyuncu1) >8 :
    print("daha kısa bir isim giriniz")

elif len(oyuncu2) >8 :
   print("daha kısa bir isim giriniz")


else:
    print("onaylandı")

silahsecimi1 = input(" bir silah seçiniz : ")
silahsecimi2 = input(" bir silah seçiniz : ")


if silahsecimi1 == "bıçak" or "arbalet" or "keleş" :
        print("geçersiz silah seçimi")


elif silahsecimi2 == "bıçak" or "arbalet" or "keleş" :
        print("geçersiz silah seçimi")

else:
        print("silah kuşanıldı")

