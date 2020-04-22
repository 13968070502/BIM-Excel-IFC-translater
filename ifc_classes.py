"""Definition of ifc-classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printifcrootabilities(self):
        print('The class "ifcroot" has the following abilities:')
        print('GlobalID: ', self.globalid)



class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

    def printifcobjectdefinitionabilities(self):
        print('The class "ifcobjectdefinition" has the following abilities:')
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
        print('The class "ifcobject" has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ,', self.objecttype)
        print('IsTypedBy: ', self.istypedby)



class ifcproduct(ifcobject):

    def __init__(self, globalid, name, description, objecttype, istypedby):
        super(ifcproduct, self).__init__(globalid, name, description, objecttype, istypedby)

    def printifcproductabilities(self):
        print('The class "ifcproduct" has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ,', self.objecttype)
        print('IsTypedBy: ', self.istypedby)



class ifcelement(ifcproduct):
    objectplacement = ""
    hasopenings = ""

    def __init__(self, globalid, name, description, objecttype, istypedby, objectplacement, hasopenings):
        super(ifcelement, self).__init__(globalid, name, description, objecttype, istypedby)
        self.objectplacement = objectplacement
        self.hasopenings = hasopenings

    def printifcelementabilities(self):
        print('The class "ifcelement" has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)
        print('ObjectPlacement: ', self.objectplacement)
        print('HasOpenings: ', self.hasopenings)



class ifcbuildingelement(ifcelement):

    def __init__(self, globalid, name, description, objecttype, istypedby, objectplacement, hasopenings,):
        super(ifcbuildingelement, self).__init__(globalid, name, description, objecttype, istypedby, objectplacement, hasopenings)

    def printifcbuildingelementabilities(self):
        print('The class "ifcbuildingelement" has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)
        print('ObjectPlacement: ', self.objectplacement)
        print('HasOpenings: ', self.hasopenings)



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
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)
        print('ObjectPlacement: ', self.objectplacement)
        print('HasOpenings: ', self.hasopenings)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('height: ', self.height)

dataifcwall = ifcwall('1234567890', 'Wall', 'vertical construction', 'Component', 'ifcbuildingelement', '0.0.0', 'Yes', '5.0', '0.2', '3.0')
dataifcwall.printifcwallabilities()

