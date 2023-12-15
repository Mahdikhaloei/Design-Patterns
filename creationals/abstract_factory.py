"""
    Abstract Factory:
        Serves to provide an interface for creating related/dependent objects without need to specify their actual class.
"""

from abc import ABC, abstractmethod


class ElectroniceProduct(ABC): # Abstract Factory
    @abstractmethod
    def call_watch(self):
        pass
    
    @abstractmethod
    def call_phone(self):
        pass


class Apple(ElectroniceProduct): # Concrete Factory1
    def call_phone(self):
        return Iphone13ProMax()
    
    def call_watch(self):
        return AppleWatchUltra49


class Samsung(ElectroniceProduct): # Concrete Factory2
    def call_phone(self):
        return GalaxyZFold5()
    
    def call_watch(self):
        return GalaxyWatch6()


class Watch(ABC): #Abstract Product A
    @abstractmethod
    def create_watch(self):
        pass


class Phone(ABC): #Abstract Product B
    @abstractmethod
    def create_phone(self):
        pass


class AppleWatchUltra49(Watch): # product A1
    def create_watch(self):
        print("this is your watch apple watch ultra 49...")


class GalaxyWatch6(Watch): # product A2
    def create_watch(self):
        print("this is your watch samsung galaxy watch 6 classic...")


class Iphone13ProMax(Phone): # product B1
    def create_phone(self):
        print("this is your iphone 13 pro max...")


class GalaxyZFold5(Phone): # product B2
    def create_phone(self):
        print("this is your galaxy z fold 5...")


def client_phone(order): # Client1
    brands = {
        "apple": Apple,
        "samsung": Samsung
    }
    phone = brands[order]().call_phone()
    phone.create_phone()


def client_watch(order): # Client2
    brands = {
        "apple": Apple,
        "samsung": Samsung
    }
    watch = brands[order]().call_watch()
    watch.create_watch()


client_phone("apple")
