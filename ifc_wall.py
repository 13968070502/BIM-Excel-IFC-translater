"""Class 'wall' with all necessary abilities"""

class ifcwall:

    """Abilities of the Class"""
    globalid = "Wall.001"
    name = "Wall"
    description = "vertical construction that bounds or subdivides spaces"
    objecttype = "Component"
    istypedby = "IfcBuildingElement"
    objectplacement = "0.0.0"
    hasopenings = "True"
    length = 5.0
    width = 0.2
    height = 3.0

    """Definition of the Constructor"""
    def __init__(self, globalid="Wall001", name="Wand", description="vertical construction that bounds or subdivides spaces", objecttype="Component",
    istypedby="IfcBuildingElement", objectplacement="0.0.0", hasopenings="True", length=5.0, width=0.2, height=3.0): # muss immer definiert werden

        """Definition of terms for the constructor"""
        self.globalid = globalid
        self.name = name
        self.description = description
        self.objecttype = objecttype
        self.istypedby = istypedby
        self.objectplacement = objectplacement
        self.hasopenings = hasopenings
        self.length = length
        self.width = width
        self.height = height

    """Output definition"""
    def printwallabilitys(self):
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('Is typed by: ', self.istypedby)
        print('Object Placement: ', self.objectplacement)
        print('Has Openings: ', self.hasopenings)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)


walldata = ifcwall("Wall.001", "Wall", "vertical construction that bounds or subdivides spaces", "Component", "IfcBuildingElement", "0.0.0", "True", 5.0, 0.2, 3.0)
walldata.printwallabilitys()