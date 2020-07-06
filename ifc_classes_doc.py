"""Ifc class model"""

"""Inheritance path of IfcPipeSegment"""
# IfcRoot
#   IfcObjectDefinition
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


"""IfcObjectDefinition"""
class IfcObjectDefinition(IfcRoot):

    def __init__(self, GlobalId):
        super(IfcObjectDefinition, self).__init__(GlobalId)


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


"""IfcProduct"""
class IfcProduct(IfcObject):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy):
        super(IfcProduct, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy)


"""IfcElement"""
class IfcElement(IfcProduct):
    ObjectPlacement = ""
    HasOpenings = ""

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy)
        self.ObjectPlacement = ObjectPlacement
        self.HasOpenings = HasOpenings


"""IfcDistributionElement"""
class IfcDistributionElement(IfcElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)


"""IfcDistributionFlowElement"""
class IfcDistributionFlowElement(IfcDistributionElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)


"""IfcFlowElement"""
class IfcFlowElement(IfcDistributionFlowElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)


"""IfcPipeSegment"""
class IfcPipeSegment(IfcFlowElement):

    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
                                                     ObjectPlacement, HasOpenings)


# Function to instantiate the class to an object

def create_IfcPipeSegment(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
    Pipe = IfcPipeSegment(GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings)
    return Pipe

# Save the object to an array
array = []
array.append(create_IfcPipeSegment('0fH7sul68HwhIZG9yu6rd_', 'Pipe', 'IfcPipe', '', 'IfcFLowSegment', '(0.0, 0.0, 0.0)', 'None'))
