# <----- HEIRARCHIAL INHERITANCE -----> #
# One Parent class and many child classes

class person:
    age = 10
    def __init__(self):
        print("Person")

class actor(person):
    def __init__(self):
        print("Actor")

class athlete(person):
    def __init__(self):
        print("Athlete")

a1 = actor()
a2 = athlete()
print(a2.age)
