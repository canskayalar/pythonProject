hesap = int(input("hoşgeldiniz hesabınız varsa 1 , yoksa 0 tuşlayın:  " ))

if hesap == 1:
   print(input("isim giriniz: "))
   print(input("şifre giriniz: "))

elif hesap == 0:
    yeniisim = print(input("yeni kullanıcı adı: "))
    yenisifre = print(input("şifre oluşturun: "))
    if len("yenisifre") > 8:
        print("daha kısa bir şifre gir")
    else:
        print("hesap oluşturuldu")
