# Definition of the class 'wall' with inherited abilities

class wall:
    name = ""
    material = ""
    length = ""
    width = ""
    height = ""

    def __init__(self, name, material, length, width, height):
        self.name = name
        self.material = material
        self.length = length
        self.width = width
        self.height = height


# Instantiation of the class 'wall' to class 'concretewall'

class concretewall(wall):
    compressivestrengthclass = ""
    exposureclass = ""

    def __init__(self, name, material, length, width, height, compressivestrengthclass, exposureclass):
        super(concretewall, self).__init__(name, material, length, width, height)
        self.compressivestrengthclass = compressivestrengthclass
        self.exposureclass = exposureclass


    def printattributes(self):
        super(concretewall, self)
        print('Name: ', self.name)
        print('Material: ', self.material)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)
        print('Compressive strength class: ', self.compressivestrengthclass)
        print('Exposure class: ', self.exposureclass)

# Data output

dataconcretewall = concretewall('Concrete wall','Concrete','5,00m','0,20m','3,00m','C25/30','XC4')
dataconcretewall.printattributes()