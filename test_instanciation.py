"""Creation of classes with inherited abilities and instantiation to an object."""

# Definition of the class 'wall' with abilities

class Wall:
    name = ""
    description = ""
    material = ""
    length = ""
    width = ""
    height = ""

    def __init__(self, name, description, material, length, width, height):
        self.name = name
        self.description = description
        self.material = material
        self.length = length
        self.width = width
        self.height = height


# Definition of class 'ReinforcedConcreteWall' with inherited and own abilities

class ReinforcedConcreteWall(Wall):
    structure = ""
    function = ""

    def __init__(self, name, description, material, length, width, height, structure, function):
        super(ReinforcedConcreteWall, self).__init__(name, description, material, length, width, height)
        self.structure = structure
        self.function = function


# Function to instantiate the class to an object

def create_ReinforcedConcreteWall(name, description, material, length, width, height, structure, function):
    Wall = ReinforcedConcreteWall(name, description, material, length, width, height, structure, function)
    return Wall

# Save the object to an array
array = []
array.append(create_ReinforcedConcreteWall('Reinforced Concrete Wall', 'STB300', 'reinforced concrete', '5,00m', '0,30m', '2,70m', 'load-bearing element', 'outside'))


# output
print(array)