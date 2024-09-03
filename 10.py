class parent:

    def __new__(cls,name,age) :
        self = super().__new__(cls)
        self.name=name
        self.age=age
        return self
    
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    
    def display(self):
        print(f"Name:{self.name},Age:{self.age}")

i1 = parent("Aarav",15)

i1.display()