"""Class 'root' with all necessary abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printrootabilitys(self):
        print('GlobalID: ', self.globalid)


class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

dataifcobjectdefinition = ifcobjectdefinition('1234567890')

dataifcobjectdefinition.printglobalid()