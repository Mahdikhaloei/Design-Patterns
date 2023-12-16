"""
    Prototype:
        Is a creational design pattern that lets ypu copy existing objects without making your code dependent on their classes.
"""

import copy


class ProtoType:
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister(self, name):
        del self._objects[name]
    
    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(kwargs)
        return obj


def client_prototype(name, obj, **kwargs):
    prototype = ProtoType()
    prototype.register_object(name, obj)
    return prototype.clone(name, **kwargs)


class Car:
    def __init__(self, company, name, model, color, **kwargs):
        self.model = model
        self.company = company
        self.name = name
        self.color = color
        self.option = []
    
    def add_option(self, option):
        self.option.append(option)


generic_car = Car("Benz", "G-Class", 2020, "black")
generic_car.add_option("V8 engin")

generic_car_clone = client_prototype("Car", generic_car, color="Yellow")

print(generic_car.__dict__)
print(generic_car_clone.__dict__)


