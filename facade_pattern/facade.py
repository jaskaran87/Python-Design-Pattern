'''
    Facade Design Pattern
    Author: Jaskaran singh
    Date 15 Aug 2018
    require: Python >= 3.4
'''
class EventManager(object):
    def __init__(self):
        print('Event Manager: Let me talk to the folk\n\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirement()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()
        
class Hotelier(object):
    def __init__(self):
        print('Arranging the hotel for marriage? --')

    def __isAvailable(self):
        print('Is the hotel free for the event on given day?')
        return True;

    def bookHotel(self):
        if self.__isAvailable():
            print('Registered the booking \n\n')

class Florist(object):
    def __init__(self):
        print('Flower decorations for the event? --')

    def setFlowerRequirement(self):
        print('Marigold, Roes and Lilies would be used for Decorations\n\n')

class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print("Indian food to be served \n\n")

class Musician(object):
    def __init__(self):
        print('Musican Arrangements for the marriage --- ')

    def setMusicType(self):
        print('Indian music will be played\n\n')

class You(object):
    def __init__(self):
        print('You:: Whoa! Marriage Arragements??!!! ')

    def askEventManager(self):
        print("You: Let's Contact with Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You: Thanks to Event Manager, all perparations done! ")

you = You()
you.askEventManager()