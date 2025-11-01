'''
01-loader-with_triads_specifications

Low-code version of the Loader model similar to the 00-loader-base_case,
but where the triad specifications are embedded in the script.

Developed by Oeystein Stranden
'''
from os import mkdir, path
from pathlib import Path

from fedempy.fmm_solver import FmmSolver
from fedempy.modeler import FedemModeler
from fedempy.enums import FmDofStat, FmLoadType, FmType

# Global constants
RELATIVE_PATH = '01-loader-with_triads_specifications/'
MODEL_FILE    = '01-loader-with_triads_specifications.fmm'
PARTS_PATH    = 'parts/'

# Note that the ftl-files do not contain the triad markers
FILES = [
    PARTS_PATH + 'Front.ftl',
    PARTS_PATH + 'Boom.ftl',
    PARTS_PATH + 'Bucket.ftl',
    PARTS_PATH + 'BellCrank.ftl',
    PARTS_PATH + 'BucketLink.ftl',
]

# Prepare run directory (=RELATIVE_PATH)
model_file = Path(RELATIVE_PATH) / MODEL_FILE
if not path.isdir(model_file.parent):
    mkdir(model_file.parent)

# Create a new FEDEM model
my_model = FedemModeler(str(model_file), force_new=True)

# Load the FE parts
parts = [my_model.make_fe_part(f) for f in FILES]
if any(p < 0 for p in parts):
    print("Failed to load FE parts")
    exit(1)

# Edit some part properties
my_model.edit_part(parts, alpha2=0.00286, component_modes=0, consistent_mass=True)

# Create functions
f1 = my_model.make_function('Lift Cylinders',
                            frequency=0.625, amplitude=0.15, delay=0.25, mean_value=0.15, end=0.8)

f2 = my_model.make_function('Boom Cylinder',
                            slope=-0.5, start_ramp=0.5, end_ramp=1.2)

f3 = my_model.make_function('Rotation Front',
                            frequency=0.5, amplitude=0.262, delay=0.25, mean_value=0.262, end=1.0)

f4 = my_model.make_function('Bucket Load',
                            slope=50000, start_ramp=0.7, end_ramp=1.2)

# Front top joint to ground
t0t = my_model.make_triad('Front_fix_bottom', node=441, on_part=parts[0])
j01 = my_model.make_joint('Rev1', FmType.REVOLUTE_JOINT, t0t)

# Front bottom joint to ground
t0b = my_model.make_triad('front_fix_top', node=211, on_part=parts[0])
j02 = my_model.make_joint('Rev2', FmType.REVOLUTE_JOINT, t0b)

# Front to boom joint on right
t0r = my_model.make_triad('front_right_housing',     node=38,  on_part=parts[0])
t1r = my_model.make_triad('boom_rear_right_houding', node=1038, on_part=parts[1])
j03 = my_model.make_joint('Rev3', FmType.REVOLUTE_JOINT, t0r, t1r)

# Front to boom joint on left
t0l = my_model.make_triad('front_left_housing',     node=58,  on_part=parts[0])
t1l = my_model.make_triad('boom_rear_left_housing', node=178, on_part=parts[1])
j04 = my_model.make_joint('Rev4', FmType.REVOLUTE_JOINT, t0l, t1l)

# Top cylinder
t0t = my_model.make_triad('front_top_cylinder_attachment', node=18, on_part=parts[0])
t3t = my_model.make_triad('bellcrank_top_housing',        node=420, on_part=parts[3])
ct  = my_model.make_spring('Boom cylinder', (t0t, t3t), init_Stiff_Coeff=1.0e9, length=f2)

# Right cylinder
t0rc = my_model.make_triad('front_right_cylinder_attachment', node=222, on_part=parts[0])
t1rc = my_model.make_triad('boom_right_cylinder_attachment',  node=829, on_part=parts[1])
cr   = my_model.make_spring('Lift cylinder', (t0rc, t1rc), init_Stiff_Coeff=1.0e9, length=f1)

# Left Cylinder
t0lc = my_model.make_triad('front_left_cylinder_attachment', node=235, on_part=parts[0])
t1lc = my_model.make_triad('boom_left_cylinder_attachment',  node=119, on_part=parts[1])
cl   = my_model.make_spring('Lift cylinder', (t0lc, t1lc), init_Stiff_Coeff=1.0e9, length=f1)

# Bocket to boom right
t1br = my_model.make_triad('boom_front_right_housing', node=715, on_part=parts[1])
t2br = my_model.make_triad('bucket_right_housing',     node=509, on_part=parts[2])
j05  = my_model.make_joint('Rev5', FmType.REVOLUTE_JOINT, t1br, t2br)

# Bocket to boom left
t1bl = my_model.make_triad('boom_front_left_housing', node=5,   on_part=parts[1])
t2bl = my_model.make_triad('bucket_left_housing',     node=284, on_part=parts[2])
j06  = my_model.make_joint('Rev6', FmType.REVOLUTE_JOINT, t1bl, t2bl)

# Bellcrank to book right|
t1rbc = my_model.make_triad('boom_right_bellcrank_housing', node=545, on_part=parts[1])
t3rbc = my_model.make_triad('bellcrank_right_housing',      node=276, on_part=parts[3])
j07   = my_model.make_joint('Rev7', FmType.REVOLUTE_JOINT, t1rbc, t3rbc)

# Bellcrank to book left
t1lbc = my_model.make_triad('boom_left_bellcrank_housing', node=424, on_part=parts[1])
t3lbc = my_model.make_triad('bellcrank_left_housing',      node=244, on_part=parts[3])
j08   = my_model.make_joint('Rev8', FmType.REVOLUTE_JOINT, t1lbc, t3lbc)

# Bucketlink rear
t3rbl = my_model.make_triad('bellcrank_bottom_housing', node=14,  on_part=parts[3])
t4rbl = my_model.make_triad('bucketlink_rear_houding',  node=575, on_part=parts[4])
j09   = my_model.make_joint('Rev9', FmType.REVOLUTE_JOINT, t3rbl, t4rbl)

# Bucketlink front
t2fbl = my_model.make_triad('bucket_mid_housing',       node=451, on_part=parts[2])
t4fbl = my_model.make_triad('bucketlink_front_housing', node=174, on_part=parts[4])
j10   = my_model.make_joint('Rev10', FmType.REVOLUTE_JOINT, t2fbl, t4fbl)

my_model.make_load('Load', FmLoadType.FORCE, 39, (0, 0, -1), fn=f4)

# Moving parts to their final location
my_model.edit_part(parts[1], Tx=0.01080263, Tz=-0.77487206)
my_model.edit_part(parts[2], Tx=-0.64636636, Tz=-2.0328088, Ry=-30, Rz=-180)
my_model.edit_part(parts[3], Tx=-3.2499752, Ty=-2.8376081, Tz=0.04694241, Ry=21.814096)
my_model.edit_part(parts[4], Tx=-2.041544, Ty=-0.92750001, Tz=0.12191465, Ry=-4.9156169)

# Joint orientation and properties
my_model.edit_joint(j01,
                    constraints={'Rz' : FmDofStat.SPRING},
                    spring={'Rz' : 1.0e9},
                    length={'Rz' : f3})
for j in [j03, j04, j05, j06, j07, j08, j09, j10]:
    my_model.edit_joint(j, Rx=90)

my_model.fm_solver_setup(t_inc=0.01, t_end=1.6)
my_model.close(True, True)

# Solver setup and execution
my_solver = FmmSolver()
my_solver.solve_all(str(model_file), True, True)
