class User:
    def __init__(self, name, surname, age):
        print("===== INIT ARGUMENTS =====")
        print("self:", self)
        print("name:", name)
        print("surname:", surname)
        print("age:", age)

        self.name = name
        self.surname = surname
        self.age = age
        
bob = User("Bob", "Smith", 11)
print("===== GLOBAL =====")
print("bob:", bob)
print("bob.name:", bob.name)
print("bob.surname:", bob.surname)
print("bob.age:", bob.age)