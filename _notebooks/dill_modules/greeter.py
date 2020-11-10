def greeting1():
    return "Booyaa!"

def greeting2():
    return "Howdy!"

class Greeter:
    def __init__(self, greetings):
        self.greetings = greetings
        
    def greet(self):
        for greet in self.greetings:
            print(greet())