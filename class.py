class student:
    def __init__(self,name,surname,number):
        self.name=name
        self.surname=surname
        self.number=number
    def show_info(self):
       print(f'isim: {self.name} , soyisim : {self.surname} , numara: {self.number}')

student1=student("cansu","kayalar","425493")
print(student1.name,student1.surname,student1.number)
student2=student("emre","korkut","425394")
print(student2.name,student2.surname,student2.number)