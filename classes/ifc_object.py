"""Definition of ifc-classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printifcrootabilities(self):
        print('GlobalID: ', self.globalid)


"""IfcObjectDefinition"""
class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

    def printifcobjectdefinitionabilities(self):
        super(ifcwall, self).printifcrootabilities()


"""IfcObject"""
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
        super(ifcwall, self).printifcobjectdefinitionabilities()
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)