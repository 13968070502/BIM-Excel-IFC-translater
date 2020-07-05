"""A program to construct a STEP-File."""

import uuid
import time
import tempfile
import ifcopenshell
from import_from_csv import get_value

# Creation of Global Unique Identifier
create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)

# Direction points to define IfcAxis2Placement
O = 0.0, 0.0, 0.0
X = 1.0, 0.0, 0.0
Y = 0.0, 1.0, 0.0
Z = 0.0, 0.0, 1.0
nX = (-1.0), 0.0, 0.0
nY = 0.0, (-1.0), 0.0
nZ = 0.0, 0.0, (-1.0)


"""Functions to generate geometry"""


# Curve
def create_ifccurve(ifcfile, axis2placement3D, radius):
    ifccurve = ifcfile.createIfcCurve(axis2placement3D, radius)
    return ifccurve


# Circle
def create_ifccircle(ifcfile, axis2placement2D, radius):
    ifccircle = ifcfile.createIfcCircle(axis2placement2D, radius)
    return ifccircle


# Cross-section of a pipe
def create_ifcarbitraryprofiledefwithvoids(ifcfile, area, area_name, outer_circle, inner_circle):
    profilewithvoids = ifcfile.createIfcArbitraryProfileDefWithVoids(area, area_name, outer_circle, inner_circle)
    return profilewithvoids


# Axis 3D
def create_ifcaxis2placement3D(ifcfile, point, dir1, dir2):
    point = ifcfile.createIfcCartesianPoint(point)
    dir1 = ifcfile.createIfcDirection(dir1)
    dir2 = ifcfile.createIfcDirection(dir2)
    axis2placement3D = ifcfile.createIfcAxis2Placement3D(point, dir1, dir2)
    return axis2placement3D


# Local placement (Location, Axis, RefDirection), specified as Python tuples, and relative placement
def create_ifclocalplacement(ifcfile, point, dir1, dir2, relative_to=None):
    axis2placement3D = create_ifcaxis2placement3D(ifcfile, point, dir1, dir2)
    ifclocalplacement = ifcfile.createIfcLocalPlacement(relative_to, axis2placement3D)
    return ifclocalplacement


# Extrusion of an area in a specific direction
def create_ifcextrudedareasolid(ifcfile, ifcclosedprofile, ifcaxis2placement3D, extrude_dir, extrusion):
    ifcdir = ifcfile.createIfcDirection(extrude_dir)
    ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(ifcclosedprofile, ifcaxis2placement3D, ifcdir, extrusion)
    return ifcextrudedareasolid


"""Construction of the file"""

# Definition of general file information
filename = get_value(1, 0) + ".ifc"
timestamp = time.time()
timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp))
creator = "Alexander Wellenhofer"
organization = "OTH Regensburg"
application, application_version = "IfcOpenShell", "0.5"
project_globalid, project_name = create_guid(), get_value(1, 0)

# Definition of constant Elements which should be included in every IFC file
template = """
ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');
FILE_NAME('%(filename)s','%(timestring)s',('%(creator)s'),('%(organization)s'),'%(application)s','%(application)s','');
FILE_SCHEMA(('IFC4'));
ENDSEC;
DATA;
#1=IFCPERSON($,$,'%(creator)s',$,$,$,$,$);
#2=IFCORGANIZATION($,'%(organization)s',$,$,$);
#3=IFCPERSONANDORGANIZATION(#1,#2,$);
#4=IFCAPPLICATION(#2,'%(application_version)s','%(application)s','');
#5=IFCOWNERHISTORY(#3,#4,$,.ADDED.,$,#3,#4,%(timestamp)s);
#6=IFCDIRECTION((1.,0.,0.));
#7=IFCDIRECTION((0.,0.,1.));
#8=IFCCARTESIANPOINT((0.,0.,0.));
#9=IFCAXIS2PLACEMENT3D(#8,#7,#6);
#10=IFCDIRECTION((0.,1.,0.));
#11=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#9,#10);
#12=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
#13=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
#14=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
#15=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
#16=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
#17=IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(0.017453292519943295),#16);
#18=IFCCONVERSIONBASEDUNIT(#12,.PLANEANGLEUNIT.,'DEGREE',#17);
#19=IFCUNITASSIGNMENT((#13,#14,#15,#18));
#20=IFCPROJECT('%(project_globalid)s',#5,'%(project_name)s',$,$,$,$,(#11),#19);
ENDSEC;
END-ISO-10303-21;
""" % locals()  # Method, which updates and returns a dictionary

# Write the elements to a temporary file
temp_handle, temp_filename = tempfile.mkstemp(suffix=".ifc")
with open(temp_filename, "w") as f:
    f.write(template)

# Obtain references to instances defined in template
ifcfile = ifcopenshell.open(temp_filename)
owner_history = ifcfile.by_type("IfcOwnerHistory")[0]
project = ifcfile.by_type("IfcProject")[0]
context = ifcfile.by_type("IfcGeometricRepresentationContext")[0]

# IFC hierarchy creation (site, building, storey)
site_placement = create_ifclocalplacement(ifcfile, O, Z, X)
site = ifcfile.createIfcSite(create_guid(), owner_history, "Site", None, None, site_placement, None, None, "ELEMENT",
                             None, None, None, None, None)

building_placement = create_ifclocalplacement(ifcfile, O, Z, X, relative_to=site_placement)
building = ifcfile.createIfcBuilding(create_guid(), owner_history, 'Building', None, None, building_placement, None,
                                     None, "ELEMENT", None, None, None)

storey_placement = create_ifclocalplacement(ifcfile, O, Z, X, relative_to=building_placement)
elevation = 0.0
building_storey = ifcfile.createIfcBuildingStorey(create_guid(), owner_history, 'Storey', None, None, storey_placement,
                                                  None, None, "ELEMENT", elevation)

container_storey = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Building Container", None, building,
                                                  [building_storey])
container_site = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Site Container", None, site, [building])
container_project = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Project Container", None, project,
                                                   [site])


# ______________________________________________________________________________________________________________________

def create_pipe(name, description, outer_radius, inner_radius, material, origin_point, direction):

    # Construction of geometry by extrusion of IfcArbitraryProfileDefWithVoids (two IfcCircles)
    object_placement = create_ifclocalplacement(ifcfile, origin_point, direction, Z, relative_to=storey_placement)
    outer_circle = create_ifccircle(ifcfile, object_placement, outer_radius)  # Outer circle
    inner_circle = create_ifccircle(ifcfile, object_placement, inner_radius)  # Inner circle
    profile = create_ifcarbitraryprofiledefwithvoids(ifcfile, "AREA", "Pipe Profile", outer_circle,
                                                     [inner_circle])  # Profile Definition
    solid = create_ifcextrudedareasolid(ifcfile, profile, object_placement, (0.0, 0.0, 1.0), 10.0)  # Extrusion
    body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

    product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [body_representation])
    pipe = ifcfile.createIfcPipeSegment(create_guid(), owner_history, name, description, None, object_placement,
                                        product_shape, None, None)

    # Define and associate the object material
    material = ifcfile.createIfcMaterial(material)
    material_layer = ifcfile.createIfcMaterialLayer(material, 0.2, None)
    material_layer_set = ifcfile.createIfcMaterialLayerSet([material_layer], None)
    material_layer_set_usage = ifcfile.createIfcMaterialLayerSetUsage(material_layer_set, "AXIS2", "POSITIVE", -0.1)
    ifcfile.createIfcRelAssociatesMaterial(create_guid(), owner_history, RelatedObjects=[pipe],
                                           RelatingMaterial=material_layer_set_usage)

    # Relate the object to the building storey
    ifcfile.createIfcRelContainedInSpatialStructure(create_guid(), owner_history, "Building Storey Container", None,
                                                    [pipe],
                                                    building_storey)


# create_pipe(Object_Name = 1; Object_Id = 2; Outer_Radius = 4; Inner_Radius = 5; Material=8; X_start = 9; Y_start = 10; Z_start=11; X_end = 12; Y_end = 13; Z_end=14; Direction=15
create_pipe(get_value(1, 1), get_value(1, 2), float(get_value(1, 4)), float(get_value(1, 5)), get_value(1, 8), (float(get_value(1, 10)), float(get_value(1, 11)), float(get_value(1, 12))), X)
create_pipe(get_value(2, 1), get_value(2, 2), float(get_value(2, 4)), float(get_value(2, 5)), get_value(2, 8), (float(get_value(2, 10)), float(get_value(2, 11)), float(get_value(2, 12))), Y)
create_pipe(get_value(3, 1), get_value(3, 2), float(get_value(3, 4)), float(get_value(3, 5)), get_value(3, 8), (float(get_value(3, 10)), float(get_value(3, 11)), float(get_value(3, 12))), nX)
create_pipe(get_value(4, 1), get_value(4, 2), float(get_value(4, 4)), float(get_value(4, 5)), get_value(4, 8), (float(get_value(4, 10)), float(get_value(4, 11)), float(get_value(4, 12))), Y)
create_pipe(get_value(5, 1), get_value(5, 2), float(get_value(5, 4)), float(get_value(5, 5)), get_value(5, 8), (float(get_value(5, 10)), float(get_value(5, 11)), float(get_value(5, 12))), nX)
create_pipe(get_value(6, 1), get_value(6, 2), float(get_value(6, 4)), float(get_value(6, 5)), get_value(6, 8), (float(get_value(6, 10)), float(get_value(6, 11)), float(get_value(6, 12))), nY)
# ______________________________________________________________________________________________________________________



# Write the contents of the file to disk
ifcfile.write(filename)
