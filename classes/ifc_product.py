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

    def print_ifcobject_abilities(self):
        super(ifcwall, self).printifcobjectdefinitionabilities()
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)


"""IfcProduct"""
class ifcproduct(ifcobject):

    def __init__(self, globalid, name, description, objecttype, istypedby):
        super(ifcproduct, self).__init__(globalid, name, description, objecttype, istypedby)

    def print_ifcproduct_abilities(self):
        super(ifcwall, self).printifcobjectabilities()

