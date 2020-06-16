"""Class 'root' with all necessary abilities"""

class ifcroot:

    """Abilities of the Class"""
    globalid = "1234567890"

    """Definition of the Constructor"""
    def __init__(self, globalid="Wall001"):

        """Definition of terms for the constructor"""
        self.globalid = globalid

    """Output definition"""
    def print_ifcroot_abilitys(self):
        print('GlobalID: ', self.globalid)

dataifcroot = ifcroot("1234567890")
dataifcroot.printifcrootabilitys()