class cars:
    def  __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def displaycars(self):
        print("name"+self.name)
        print("price",self.price)
        print("color"+self.color)
car1=cars("Thar",1750000,"black")
car2=cars("Jimny",1200000,"green")
car1.displaycars()
car2.displaycars()
        
