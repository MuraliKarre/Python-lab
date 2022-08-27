class Mammel:
    def walk(self):
        print("walk")


class Dog(Mammel):
    def bowbow(self):
        print("BowBOW")
      

class Cat(Mammel):
    def meowmmeowm(self):
        print("meowmmeowm")

cat1 = Cat() 
cat1.meowmmeowm()
cat1.walk()


dog1 = Dog()
dog1.bowbow()
dog1.walk()