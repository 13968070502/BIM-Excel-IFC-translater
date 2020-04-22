"""Class 'root' with all necessary abilities"""

class ifcroot:

    """Abilities of the Class"""
    GlobalId = "Wall.001"

    """Definition of the Constructor"""
    def __init__(self, GlobalId1="Wall001"):

        """Definition of terms for the constructor"""
        self.GlobalId1 = GlobalId1

    """Output definition"""
    def printrootabilitys(self):
        print('GlobalID1: ', self.GlobalId)

WallData = ifcroot("Wall.001")
WallData.printrootabilitys()