class Mother:
    def print(self):
        print(self.age(), self.sex())
    
    def age(self):
        return "43"

    def sex(self):
        return "female"

m = Mother()
print ("Mum: ")
m.print()

class Son(Mother):
    def age(self):
        return "18"

    def sex(self):
        return "male"

s = Son()
print ("Son: ")
s.print()
