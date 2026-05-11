class Pen:
    def __init__(self,colour,brand,type,price):
        self.colour = colour
        self.brand = brand
        self.type = type
        self.price = price
        self.ink_level=100
        
        def write(self,text):
            if self.ink_level>10:
                return f" number of characters written {len(self.text)}"  
            elif self.ink_level>0:
                return f" number of characters written {self.ink_level//10}"   
            else:
                return "ink is not enough to write"
            
        def capacity(self,ink_level):
            self.ink_level=self.ink_level-10*len(self.text)
            
        def refilled(self):
            if self.ink_level==100:
                return "pen is already full"
            elif self.ink_level==0:
                return "need to refill the pen"
            else:
                return f" number of characters written {len(self.text)}"
        
        def choose_colur(self,colour):
            self.colour=colour
            
        def type_of_pen(self,type):
            self.type=type
            
        def price_of_pen(self,price):
            self.price=price
            
        def brand_of_pen(self,brand):
            self.brand=brand
            
            
        def Is_floatable(self):
            if self.type=="ball":
                return "pen is floatable"
            else:
                return "pen is not floatable"
            
        def is_reusable(self):
            if self.type=="ball":
                return "pen is reusable"
            else:
                return "pen is not reusable"
            
#inheritance           
            
class beautifY_text(Pen):
    def all_features(self):
        super().write()
        super().refilled()
        super().choose_colur()
        super().type_of_pen()
        if self.type=="ball":
            super().Is_floatable()
            super().is_reusable()
            print("more beautiful text can be written")
        else:
            if super().write()!="ink is not enough to write":
                print("beautiful text can be written")
            
#Abstaction
class encapsulationing_pen(Pen):
    def product_visible_information_in_nonreusable_pen(self):
        super().__capacity(self.ink_level)
        return f"colour of pen is {self.colour} and brand of pen is {self.brand} and type of pen is {self.type} and price of pen is {self.price}"
    
#Encapsulation
class all_features_contain(Pen):
    def all_features(self):
        super().write()
        super().refilled()
        super().choose_colur()
        super().type_of_pen()
        if self.type=="ball":
            super().Is_floatable()
            super().is_reusable()
            print("more beautiful text can be written")
        else:
            if super().write()!="ink is not enough to write":
                print("beautiful text can be written")
                
                
#Polymorphism

class laser_pointer:
    def __init__(self,colour,brand,type,price):
        self.colour = colour
        self.brand = brand
        self.type = type
        self.price = price
       
    def pointer(self):
        return "laser pointer is used for presentation"
    

        
            
                          
                          
                          
object1=Pen("blue","cello","ball",10)
