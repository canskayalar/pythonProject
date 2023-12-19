class calisan:
    def __init__(self,name,surname,age):
        self.name= name
        self.surname=surname
        self.age= age
    def show_info(self):
        print(f'ad:{self.name}   soyad:{self.surname}   yaş:{self.age}')

calisan1=calisan("ali","veli" ,20)
print(calisan1.name, calisan1.surname,calisan1.age)
calisan2=calisan("mehmet","ahmet" ,25)
print(calisan2.name, calisan2.surname,calisan2.age)