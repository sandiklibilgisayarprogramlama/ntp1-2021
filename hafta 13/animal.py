class Animal:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    def set_name(self,new_name):
        self.name = new_name
    
    def eat(self):
        print("yedi")