"""Definition of ifc-classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def print_ifcroot_abilities(self):
        print('GlobalID: ', self.globalid)


"""IfcObjectDefinition"""
class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

    def print_ifcobjectdefinition_abilities(self):
        super(ifcwall, self).printifcrootabilities()

