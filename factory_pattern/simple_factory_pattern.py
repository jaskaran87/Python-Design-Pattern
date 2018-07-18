from abc import ABCMeta, abstractmethod

class Animal (metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass
    
class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")

## forest Factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()



# client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)

'''
    Please provide input, do not make typo error 
    1) Dog 
    2) Cat

    # eval = The eval() method returns the result evaluated from the expression 
    eval(object_type)()
    with the help of Eval, it will change into: Dog()
    example: 
    x = 1
    print(eval('x + 1')) 
    output: 2
'''