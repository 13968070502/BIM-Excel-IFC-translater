# IfcRoot
# IfcObjectDefinition
# IfcObject
# IfcProduct
# IfcElement
# IfcDistributionElement
# IfcDistributionFlowElement
# IfcFlowSegment
# IfcPipeSegment

"""Definition of class IfcPipeSegment with inherited abilities"""
class IfcRoot:
    GlobalId = ""

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
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings)

    def print_IfcDistributionElement_abilities(self):
        super(IfcDistributionElement, self).print_IfcElement_abilities()


"""IfcDistributionFlowElement"""
class IfcDistributionFlowElement(IfcDistributionElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings)

    def print_IfcDistributionFlowElement_abilities(self):
        super(IfcDistributionFlowElement, self).print_IfcDistributionElement_abilities()


"""IfcFlowSegment"""
class IfcFlowSegment(IfcDistributionFlowElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings)

    def print_IfcFlowSegment_abilities(self):
        super(IfcFlowSegment, self).print_IfcDistributionElement_abilities()


"""IfcPipeSegment"""
class IfcPipeSegment(IfcFlowSegment):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings)

    def print_IfcPipeSegment_abilities(self):
        super(IfcPipeSegment, self).print_IfcDistributionElement_abilities()

data_IfcPipeSegment = IfcPipeSegment('1234567890123456789012', 'Pipe', 'Heating', 'Flow Element', 'IfcFlowSegment', '0.0.0', 'No')
data_IfcPipeSegment.print_IfcPipeSegment_abilities()

