class Car:
    def __init__(self,model,color,year):
        self.model=model
        self.color=color
        self.year=year
    def launch(self):
        print(f'{self.model} launched in {self.year} with {self.color} color')
class subategory:
    def subcat(self):
        self.subcat='SUV'
class inherit(Car,subategory):
    def __init__(self,model,color,year):
        super().__init__(model,color,year)
s=Car('BMW','Black',2020)
s.launch()
print(s.model)
print(s.color)  
print(s.year)
new_car=Car('Audi','White',2011)
v=inherit('Tata',"Red",2015)
v.launch()
v.subcat()

print(new_car.model)
print(new_car.color)
print(new_car.year)