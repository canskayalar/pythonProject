print("oyuncu kaydetme programı")
ad = input("oyuncunun adı :  ")
soyad = input("oyunucunun soyadı : ")
yas = input("oyuncunun yaşı : ")
takim = input("oyuncunun takımı : ")

bilgiler = [ad,soyad,yas,takim]

print("database'e kaydediliyor... ")
print("oyuncu adı:{} oyuncu soyadı:{} oyuncu yaşı:{} oyuncu takımı:{}" .format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3]))

print("kaydedildi!")
