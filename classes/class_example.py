# Definition of the class 'wall' with some abilities

class Wall:
    name = ""
    designation = ""
    material = ""
    length = ""
    width = ""
    height = ""

    def __init__(self, name, designation, material, length, width, height):
        self.name = name
        self.designation = designation
        self.material = material
        self.length = length
        self.width = width
        self.height = height


# Instantiation of the class 'Wall' to class 'ReinforcedConcreteWall' with inherited abilities

class ReinforcedConcreteWall(Wall):
    structure = ""
    function = ""

    def __init__(self, name, designation, material, length, width, height, structure, function):
        super(ReinforcedConcreteWall, self).__init__(name, designation, material, length, width, height)
        self.structure = structure
        self.function = function

# Method to print attributes of the class

    def printattributes(self):
        super(ReinforcedConcreteWall, self)
        print('Name: ', self.name)
        print('Designation: ', self.designation)
        print('Material: ', self.material)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)
        print('Structure: ', self.structure)
        print('Function: ', self.function)

# Data output

get_data = ReinforcedConcreteWall('Reinforced Concrete Wall', 'STB300', 'reinforced concrete','5,00m','0,30m','2,70m','load-bearing element','outside')
get_data.printattributes()