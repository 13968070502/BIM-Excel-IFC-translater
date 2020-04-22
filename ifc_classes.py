"""Definition of ifc-classes with inherited abilities"""

class ifcroot:
    globalid = ""

    def __init__(self, globalid):
        self.globalid = globalid

    def printifcrootabilities(self):
        print('The ifc-class has the following abilities:')
        print('GlobalID: ', self.globalid)



class ifcobjectdefinition(ifcroot):

    def __init__(self, globalid):
        super(ifcobjectdefinition, self).__init__(globalid)

    def printifcobjectdefinitionabilities(self):
        print('The ifc-class has the following abilities:')
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
        print('The ifc-class has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ,', self.objecttype)
        print('IsTypedBy: ', self.istypedby)



class ifcproduct(ifcobject):

    def __init__(self, globalid, name, description, objecttype, istypedby):
        super(ifcproduct, self).__init__(globalid, name, description, objecttype, istypedby)

    def printifcproductabilities(self):
        print('The ifc-class has the following abilities:')
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
        print('The ifc-class has the following abilities:')
        print('GlobalID: ', self.globalid)
        print('Name: ', self.name)
        print('Description: ', self.description)
        print('ObjectType: ', self.objecttype)
        print('IsTypedBy: ', self.istypedby)
        print('ObjectPlacement: ', self.objectplacement)
        print('HasOpenings: ', self.hasopenings)


dataifcelement = ifcelement('1234567890', 'Wall', 'vertical construction', 'Component', 'ifcproduct', '0.0.0', 'Yes')
dataifcelement.printifcelementabilities()