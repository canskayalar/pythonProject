class araba:
    def __init__(self, model,tarih,renk):
        self.model=model
        self.tarih=tarih
        self.renk=renk


mercedes=araba("amg" , 2020 , "beyaz" )
print("mercedes" ,mercedes.model,mercedes.tarih,mercedes.renk)
bmw=araba("x6" , 2019 , "siyah")
print("bmw" ,bmw.model,bmw.tarih,bmw.renk)
audi=araba("A4" , 2018 , "kırmızı")
print("audi" ,audi.model,audi.tarih,audi.renk)
