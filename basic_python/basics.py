def basic(name:str):
    return f"Hello {name} welcome to python basics"
print(basic("aakanksha"))
def num(a:float,b:float)->float:    

    return a+b
print(num(2.5,3.5))

class Car:
    def __init__(self,make:str,model:str,year:int)->None:
        self.make=make
        self.model=model
        self.year=year
    def start_engine(self):
        return f"{self.make} {self.model} engine started"
        
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
volvo:Car=Car("Toyota","Camry",2020)
print(volvo.start_engine())
BMW:Car=Car("BMW","X5",2021)
print(BMW.get_info())