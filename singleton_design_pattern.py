class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print('Singleton Class Object', s1)
print('----------------------------')
print('Singleton Class Object', s2)
