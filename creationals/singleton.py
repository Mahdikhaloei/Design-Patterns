"""
    Singleton:
        --> Ensure a class only has one instance, and provide a global point of access to it.
"""

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class LifeChoices(metaclass=SingletonMeta):
    def __init__(self):
        self.choice = None
    
    def make_choice(self, option):
        if not self.choice:
            self.choice = option
            print(f"You have chosen: {self.choice}")
        else:
            print(f"Sorry, your life choice is already set: {self.choice}")


life_choices1 = LifeChoices()
life_choices2 = LifeChoices()

life_choices1.make_choice("Becoming a millionaire")
life_choices2.make_choice("lie off!")

life_choices1.make_choice("going to party!")

print(life_choices1 == life_choices2)
