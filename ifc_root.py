# Class "root" with all necessary abilities

class IfcRoot:
    """Abilities of the Class"""
    GlobalId = "Wall.001"
    Name = "Wall"
    Description = "vertical construction that bounds or subdivides spaces"
    ObjectType = "Component"
    isTypedBy = "IfcBuildingElement"
    ObjectPlacement = 0.0
    HasOpenings = "Yes"
    length = 5.0
    width = 0.2
    height = 3.0

    """Definition of the Constructor"""

    def __init__(self, GlobalId="Wall001", Name="Wand",
                 Description="vertical construction that bounds or subdivides spaces", ObjectType="Component",
                 isTypedBy="IfcBuildingElement", ObjectPlacement=0.0, HasOpenings="Yes", length=5.0, width=0.2,
                 height=3.0):  # muss immer definiert werden

        # Definition of the __init__ Constructor terms
        self.GlobalId = GlobalId
        self.Name = Name
        self.Description = Description
        self.ObjectType = ObjectType
        self.isTypedBy = isTypedBy
        self.ObjectPlacement = ObjectPlacement
        self.HasOpenings = HasOpenings
        self.length = length
        self.width = width
        self.height = height

    """Output definition"""
    def printWallAbilitys(self):
        print('GlobalID: ', self.GlobalId)
        print('Name: ', self.Name)
        print('Description: ', self.Description)
        print('ObjectType: ', self.ObjectType)
        print('Is typed by: ', self.isTypedBy)
        print('Object Placement: ', self.ObjectPlacement)
        print('Has Openings: ', self.HasOpenings)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)


WallData = ifcwall("Wall.001", "Wall", "vertical construction that bounds or subdivides spaces", "Component",
                   "IfcBuildingElement", 0.0, "Yes", 5.0, 0.2, 3.0)
WallData.printWallAbilitys()