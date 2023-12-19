class dusman():
    def __init__(self,ordu_adi,silah,kisi_sayisi):
        self.ordu_adi=ordu_adi
        self.silah=silah
        self.kisi_sayisi=kisi_sayisi
    def print(self):
        print(f"ordu1: {self.ordu_adi}  silah1: {self.silah}  kişi: {self.kisi_sayisi}")

ordu1=dusman("korsanlar","arbalet",300)
print(ordu1.ordu_adi,ordu1.silah,ordu1.kisi_sayisi)


class dost():
    def __init__(self,ordu_adi2,silah2,kisi_sayisi2):
        self.ordu_adi2=ordu_adi2
        self.silah2=silah2
        self.kisi_sayisi2=kisi_sayisi2

    def print(self):
        print(f"ordu1: {self.ordu_adi2}  silah1: {self.silah2}  kişi: {self.kisi_sayisi2}")

ordu2=dusman("melekler","roket",250)
print(ordu2.ordu_adi,ordu2.silah,ordu2.kisi_sayisi)

print("savaş başlatılıyor...")

hasar = (int(input("düşmanlar için vuruş sayısı girin: ")))
toplamcan1=100
toplamcan2=100

if toplamcan1 != 0 :
    for toplamcan1 in range(100,toplamcan1-1,-1):
            toplamcan1 -= 2 * hasar
            print(toplamcan1)










