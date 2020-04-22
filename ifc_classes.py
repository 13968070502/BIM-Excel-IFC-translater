"""Class 'root' with all necessary abilities"""

class ifcroot:

    """Abilities of the Class"""
    GlobalId = "Wall.001"

    """Definition of the Constructor"""
    def __init__(self, GlobalId="Wall001"):

        """Definition of terms for the constructor"""
        self.GlobalId1 = GlobalId

    """Output definition"""
    def printrootabilitys(self):
        print('GlobalID: ', self.GlobalId)


"""Class 'wall' with an inherited ability"""
class ifcwall(ifcroot):

    """Abilities of the Class"""
    name = "Wall"

    """Definition of the Constructor"""
    def __init__(self, GlobalId="Wall001", Name="Wand"):
        super(ifcwall, self).__init__(GlobalId)
        self.Name



