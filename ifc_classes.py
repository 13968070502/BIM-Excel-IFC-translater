"""Ifc class model"""

from import_from_csv import get_value
from create_guid import create_GUID

"""Inheritance path of IfcPipeSegment"""

# IfcRoot
#   IfcObjectDefinition#
#       IfcObject
#           IfcProduct
#               IfcElement
#                   IfcDistributionElement
#                       IfcDistributionFlowElement
#                           IfcFlowSegment
#                               IfcPipeSegment

"""Definition of class IfcPipeSegment with inherited abilities"""


class IfcRoot:
    GlobalId = ''

    def __init__(self, GlobalId):
        self.GlobalId = GlobalId

    def print_IfcRoot_abilities(self):
        print('GlobalID: ', self.GlobalId)


"""IfcObjectDefinition"""


class IfcObjectDefinition(IfcRoot):

    def __init__(self, GlobalId):
        super(IfcObjectDefinition, self).__init__(GlobalId)

    def print_IfcObjectDefinition_abilities(self):
        super(IfcObjectDefinition, self).print_IfcRoot_abilities()


"""IfcObject"""


class IfcObject(IfcObjectDefinition):
    Name = ""
    Description = ""
    ObjectType = ""
    IsTypedBy = ""

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy):
        super(IfcObject, self).__init__(GlobalId)
        self.Name = Name
        self.Description = Description
        self.ObjectType = ObjectType
        self.IsTypedBy = IsTypedBy

    def print_IfcObject_abilities(self):
        super(IfcObject, self).print_IfcObjectDefinition_abilities()
        print('Name: ', self.Name)
        print('Description: ', self.Description)
        print('ObjectType: ', self.ObjectType)
        print('IsTypedBy: ', self.IsTypedBy)


"""IfcProduct"""


class IfcProduct(IfcObject):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy):
        super(IfcProduct, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy)

    def print_IfcProduct_abilities(self):
        super(IfcProduct, self).print_IfcObject_abilities()


"""IfcElement"""


class IfcElement(IfcProduct):
    ObjectPlacement = ""
    HasOpenings = ""

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy)
        self.ObjectPlacement = ObjectPlacement
        self.HasOpenings = HasOpenings

    def print_IfcElement_abilities(self):
        super(IfcElement, self).print_IfcProduct_abilities()
        print('ObjectPlacement: ', self.ObjectPlacement)
        print('HasOpenings: ', self.HasOpenings)


"""IfcDistributionElement"""


class IfcDistributionElement(IfcElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)

    def print_IfcDistributionElement_abilities(self):
        super(IfcDistributionElement, self).print_IfcElement_abilities()


"""IfcDistributionFlowElement"""


class IfcDistributionFlowElement(IfcDistributionElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)

    def print_IfcDistributionFlowElement_abilities(self):
        super(IfcDistributionFlowElement, self).print_IfcDistributionElement_abilities()


"""IfcFlowElement"""


class IfcFlowElement(IfcDistributionFlowElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)

    def print_IfcFlowElement_abilities(self):
        super(IfcFlowElement, self).print_IfcDistributionElement_abilities()


"""IfcPipeElement"""


class IfcPipeSegment(IfcFlowElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)

    def print_IfcPipeSegment_abilities(self):
        super(IfcPipeSegment, self).print_IfcDistributionElement_abilities()


# Instantiation - creating an object out of a class
PipeSegment = IfcPipeSegment(create_GUID(), get_value(1, 1), get_value(1, 2), get_value(1, 8), get_value(1,3), '0.0.0', 'No')

PipeSegment.print_IfcPipeSegment_abilities()

# Define headers
# Object=0; Object_Id=1; IFC_Element=2; Diameter=3; Material=4; Pipe_Color=5; Piping_type=6; H_V=7;
# Total_vertices=8; X_min=9; Y_min=10; X_max=11; Y_max=12; Project=13; Building=14; Floor=15; Room=16
