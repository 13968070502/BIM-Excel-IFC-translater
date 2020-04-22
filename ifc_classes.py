"""Classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printifcrootabilities(self):
        print('GlobalID: ', self.globalid)



class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

    def printifcobjectdefinitionabilities(self):
        print('GlobalID: ', self.globalid)



class ifcobject(ifcobjectdefinition):
    name = ""
    description = ""
    objecttype = ""
    istypedby = ""

    def __init__(self, globalid, name, description, objecttype, istypedby):
        super(ifcobject, self).__init__(globalid)
        self.name = name
        self.description = description
        self.objecttype = objecttype
        self.istypedby = istypedby

    def printifcobjectabilities(self):
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('Objecttpe: ,', self.objecttype)
        print('IsTypedBy: ', self.istypedby)

dataifcobject = ifcobject('1234567890', 'Wall', 'vertical construction', 'Component', 'ifcobjectdefinition')
dataifcobject.printifcobjectabilities()

