from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print('Personal Section')
    
class AlbumSection(Section):
    def describe(self):
        print("Personal Section")

class PatentSection(Section):
    def describe(self):
        print("Album Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, sections):
        self.sections.append(sections)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(Publication())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == '__main__':
    profile_type = input ('Which Profile you would like to create [Linkedin or Facebook]?')
    profile = eval(profile_type.lower())()
    print('Creating Profile..', type(profile).__name__)
    print("Profile has sections --", profile.getSections())

