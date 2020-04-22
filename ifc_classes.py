"""Definition of ifc-classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printifcrootabilities(self):
        print('GlobalID: ', self.globalid)


"""IfcIbjectDefinition"""
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
        print('ObjectType: ,', self.objecttype)
        print('IsTypedBy: ', self.istypedby)


"""IfcProduct"""
class ifcproduct(ifcobject):

    def __init__(self, globalid, name, description, objecttype, istypedby):
        super(ifcproduct, self).__init__(globalid, name, description, objecttype, istypedby)

    def printifcproductabilities(self):
        super(ifcwall, self).printifcobjectabilities()


"""IfcElement"""
class ifcelement(ifcproduct):
    objectplacement = ""
    hasopenings = ""

    def __init__(self, globalid, name, description, objecttype, istypedby, objectplacement, hasopenings):
        super(ifcelement, self).__init__(globalid, name, description, objecttype, istypedby)
        self.objectplacement = objectplacement
        self.hasopenings = hasopenings

    def printifcelementabilities(self):
        super(ifcwall, self).printifcproductabilities()
        print('ObjectPlacement: ', self.objectplacement)
        print('HasOpenings: ', self.hasopenings)


"""ifcBuildingElement"""
class ifcbuildingelement(ifcelement):

    def __init__(self, globalid, name, description, objecttype, istypedby, objectplacement, hasopenings,):
        super(ifcbuildingelement, self).__init__(globalid, name, description, objecttype, istypedby, objectplacement, hasopenings)

    def printifcbuildingelementabilities(self):
        super(ifcwall, self).printifcelementabilities()


"""IfcWall"""
class ifcwall(ifcbuildingelement):
    length = ""
    width = ""
    height = ""

    def __init__(self, globalid, name, description, objecttype, istypedby, objectplacement, hasopenings, length, width, height):
        super(ifcwall, self).__init__(globalid, name, description, objecttype, istypedby, objectplacement, hasopenings)
        self.length = length
        self.width = width
        self.height = height

    def printifcwallabilities(self):
        print('The class "ifcwall" has the following abilities:')
        super(ifcwall, self).printifcbuildingelementabilities()
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('height: ', self.height)

dataifcwall = ifcwall('1234567890', 'Wall', 'vertical construction', 'Component', 'ifcbuildingelement', '0.0.0', 'Yes', '5.0', '0.2', '3.0')
dataifcwall.printifcwallabilities()
