kenar = float(input("kenar sayısı girin: "))
pi = 3.14


if kenar==0 :
    print("çember")
    r = float(input("yarıçap gir: "))
    alancember = pi*(r**2)
    print(f'(alancember) {alancember}')



elif kenar==3 :
    print("üçgen")
    taban = float(input("taban uzunluğu: "))
    yukseklik = float(input("yükseklik: "))
    alanucgen = taban * yukseklik / 2
    print(f'(alanucgen) {alanucgen}')


elif kenar==4 :
    print("dörtgen")
    taban = float(input("taban uzunluğu: "))
    yukseklik = float(input("yükseklik: "))
    alandortgen = taban * yukseklik
    print(f'(alandortgen) {alandortgen}')






