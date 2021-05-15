class Car(object):
    def __init__ (self,name,speed,weight,color,raiting):
        self.name=name
        self.speed=speed
        self.weight=weight
        self.color=color
        self.raiting=raiting

    def display(self):
        print(self.name,self.speed,self.weight,self.color,self.raiting)
car1=Car("Nano",50,320,"red",3.5)  
car2=Car("Audi",250,400,"blue",4.5) 
car1.display()   
car2.display()
dicitionary1={
    "carname":"Toyata",
    "year":2021
}
print(dicitionary1["carname"])
list1=["toyota","2021"]
print(list1[0])