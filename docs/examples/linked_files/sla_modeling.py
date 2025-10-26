'''
02-car-front-suspension

Low-code version of the car front suspension model (Short-Long Arm).

Developed by Knut Morten Okstad (kmo@openfedem.org)
'''

from os import mkdir, path
from pathlib import Path

from fedempy.modeler import FedemModeler
from fedempy.enums import FmDof, FmDofStat, FmType, FmVar

# Global constants
RELATIVE_PATH = '02-car-front-suspension/'
MODEL_FILE    = '02-sla-dtwin.fmm'
PARTS_PATH    = 'parts/'

# Prepare run directory (=RELATIVE_PATH)
model_file = Path(RELATIVE_PATH) / MODEL_FILE
if not path.isdir(model_file.parent):
    mkdir(model_file.parent)

# Create a new FEDEM model
my_model = FedemModeler(str(model_file), force_new=True)

# Load the FE parts
lca     = my_model.make_fe_part(PARTS_PATH + 'lca.nas')
knuckle = my_model.make_fe_part(PARTS_PATH + 'knuckle.nas')
uca     = my_model.make_fe_part(PARTS_PATH + 'uca.nas')
ground  = 2  # base id of the reference plane will always be 2

# Lower control arm joints to ground
j1 = my_model.make_joint('Fix 1', FmType.BALL_JOINT,
                         my_model.make_triad('lca fixed', node=11911, on_part=lca))
j2 = my_model.make_joint('Fix 2', FmType.BALL_JOINT,
                         my_model.make_triad('lca fixed', node=11912, on_part=lca))

# Knuckle to lower control arm joint
j3 = my_model.make_joint('Lower Ball', FmType.BALL_JOINT,
                         my_model.make_triad('knuckle lower', node=3, on_part=knuckle),
                         my_model.make_triad('lca tip',   node=11910, on_part=lca))

# Upper control arm to knuckle joint
j4 = my_model.make_joint('Upper Ball', FmType.BALL_JOINT,
                         my_model.make_triad('uca tip',    node=2160, on_part=uca),
                         my_model.make_triad('knuckle upper', node=4, on_part=knuckle))

# Upper control arm joints to ground
j5 = my_model.make_joint('Fix 3', FmType.BALL_JOINT,
                         my_model.make_triad('uca fixed',  node=2159, on_part=uca))
j6 = my_model.make_joint('Fix 4', FmType.BALL_JOINT,
                         my_model.make_triad('uca fixed',  node=2158, on_part=uca))

# Steering pin triad
t0 = my_model.make_triad('Steering pin', node=2, on_part=knuckle)
my_model.edit_triad(t0, constraints={'Tx' : FmDofStat.FIXED})

# Damper
t1 = my_model.make_triad('Damper pin', node=11909, on_part=lca)
t2 = my_model.make_triad('Damper ground', pos=(0.0, 0.0, 0.3), on_part=ground)
s1 = my_model.make_spring('Damper', (t1, t2), init_Stiff_Coeff=7.5e6)
d1 = my_model.make_damper('Damper', (t1, t2), init_Damp_Coeff=3.0e3)

# Wheel hub triad with external force
t3 = my_model.make_triad('Wheel hub', node=1, on_part=knuckle)
my_model.edit_triad(t3, load={'Tz' : my_model.make_function('Wheel force')})

# Ouput sensors
o1 = my_model.make_sensor('Damper force', (s1, d1), FmVar.FORCE)
o2 = my_model.make_sensor('Damper deflection', s1, FmVar.DEFLECTION)
o3 = my_model.make_sensor('Steering pin deflection', t0, FmVar.POS, FmDof.TZ)

my_model.fm_solver_setup(t_inc=0.005, t_end=2.5, t_quasi=-1.0)
my_model.fm_solver_tol(1.0e-6,1.0e-6,1.0e-6)
my_model.close(True, True)
