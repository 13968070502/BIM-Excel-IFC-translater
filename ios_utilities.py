"""Usefull functions to create an IFC-File by using IfcOpenShell"""
import uuid
import time
import tempfile
import ifcopenshell

# Direction points to define IfcAxis2Placement
O = 0., 0., 0.
X = 1., 0., 0.
Y = 0., 1., 0.
Z = 0., 0., 1.
DN = 300
DN_i = 290

# Helper function definitions
# Creates an IfcAxis2Placement3D from Location, Axis and RefDirection specified as Python tuples

# Extrusion: Create shape of IfcObject by extrusion of Ifc
#201=IFCARBITRARYPROFILEWITHVOIDS(.AREA.,'Pipe Profile', #202,(#203));
#202=IFCCIRCLE(#204,0.2);
#203=IFCCIRCLE(#204,0.25);
#204=IFCAXIS2PLACEMENT2D(#205,$);
#205=IFCCARTESIANPOINT(0.0,0.2));
#206=IFCEXTRUDEDAREASOLID(#201,#204,#207,2000.0);
#207=IFCDIRECTION((0.0,1.0,0,0));
#208=IFCSHAPEREPRESENTATION(#145, 'body',$,(#206));
#501=IFCPRODUCTDEFINITIONSHAPE($,$,(#208));


# Circle
def create_ifccircle(ifcfile, point=O, radius=DN):
    radius = ifcfile.createIfcPositiveLengthMeasure(radius)
    point = ifcfile.createIfcCartesianPoint(point)
    ifccircle = ifcfile.createIfcCircle(point, radius)
    return ifccircle

# rotate solid
def create_ifcrevolvedareasolid(ifcfile, point_list, ifcaxis2placement, rotate_dir, rotation):
    polyline = create_ifcpolyline(ifcfile, point_list)
    ifcclosedprofile = ifcfile.createIfcArbitraryClosedProfileDef("AREA", None, polyline)
    ifcdir = ifcfile.createIfcDirection(rotate_dir)
    ifcrevolvedareasolid = ifcfile.createIfcRevolvedAreaSolid(ifcclosedprofile, ifcaxis2placement, ifcdir, rotation)
    return ifcrevolvedareasolid

# Axis
def create_ifcaxis1placement(ifcfile, point=O, dir2=X):
    point = ifcfile.createIfcCartesianPoint(point)
    dir2 = ifcfile.createIfcDirection(dir2)
    axis1placement = ifcfile.createIfcAxis1Placement(point, dir2)
    return axis1placement

def create_ifcaxis2placement2D(ifcfile, point=O, dir2=X):
    point = ifcfile.createIfcCartesianPoint(point)
    dir2 = ifcfile.createIfcDirection(dir2)
    axis2placement2D = ifcfile.createIfcAxis1Placement(point, dir2)
    return axis2placement2D


def create_ifcaxis2placement(ifcfile, point=O, dir1=Z, dir2=X):
    point = ifcfile.createIfcCartesianPoint(point)
    dir1 = ifcfile.createIfcDirection(dir1)
    dir2 = ifcfile.createIfcDirection(dir2)
    axis2placement = ifcfile.createIfcAxis2Placement3D(point, dir1, dir2)
    return axis2placement


# Creates an IfcLocalPlacement from Location, Axis and RefDirection, specified as Python tuples, and relative placement
def create_ifclocalplacement(ifcfile, point=O, dir1=Z, dir2=X, relative_to=None):
    axis2placement = create_ifcaxis2placement(ifcfile, point, dir1, dir2)
    ifclocalplacement2 = ifcfile.createIfcLocalPlacement(relative_to, axis2placement)
    return ifclocalplacement2


# Creates an IfcPolyLine from a list of points, specified as Python tuples
def create_ifcpolyline(ifcfile, point_list):
    ifcpts = []
    for point in point_list:
        point = ifcfile.createIfcCartesianPoint(point)
        ifcpts.append(point)
    polyline = ifcfile.createIfcPolyLine(ifcpts)
    return polyline


# Creates an IfcExtrudedAreaSolid from a list of points, specified as Python tuples
def create_ifcextrudedareasolid(ifcfile, point_list, ifcaxis2placement, extrude_dir, extrusion):
    polyline = create_ifcpolyline(ifcfile, point_list)
    ifcclosedprofile = ifcfile.createIfcArbitraryClosedProfileDef("AREA", None, polyline)
    ifcdir = ifcfile.createIfcDirection(extrude_dir)
    ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(ifcclosedprofile, ifcaxis2placement, ifcdir, extrusion)
    return ifcextrudedareasolid


create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)
