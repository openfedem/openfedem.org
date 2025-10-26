# Digital Twins models

The concept of Digital Twins of a physical asset can be modelled in FEDEM
where loads and/or actuators get their input from external sources, such as
sensors on the real asset, and produce real-time simulated response data.
The model can then be wrapped in a FMU (Functional Mockup Unit) based on the
[FMI-standard](https://fmi-standard.org) for use in a co-simulation environment.

To demonstrate how this can be done, we consider a simple car front suspension
model consisting of three FE parts:

* Lower control arm
* Upper control arm
* Knuckle

The three FE parts are connected using Ball joint objects,
while an Axial Spring and a Damper are used to represent the physical damper.

![car suspension](../images/sla_model.png)

## Digital twin input

A vertical external force is applied in the wheel hub Triad in the model.
The force magnitude is defined using an External function object in FEDEM
(indicated by the "**E**" icon in the Objects tree in the image above).
As opposed to all the other Function types which can use various response
quantities (including the time itself) as function argument, External functions
are typically assigned their value by the calling process managing the time step
loop of the numerical simulation.

## Digital twin output

In this model we want to monitor the force and deflection in the damper,
in addition to the vertical deflection of the steering pin Triad.
For this purpose, three other Function objects are defined simply as 1-to-1
functions, where the respective response quantities are defined as arguments.
These three functions (marked with the "**S**" icon in the Objects three) then
serve as virtual sensors which can be evaluated by the calling process during
the time step loop.

## Creating the digital twin using fedempy

Here is a low-code python script creating the car suspension model shown above.
The FE models used are found [here](linked_files/sla_FEparts.zip).

[Download...](linked_files/sla_modeling.py)

```python
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
```

## Exporting a FMU from FEDEM

Before the model can be exported, the FE models need to be reduced into
superelements since the FMU will only conduct the dynamics simulation
of the mechanism model. This can be done with `fedempy` using:

    $ python -m fedempy.fmm_solver -f 02-sla-dtwin.fmm --reduce-only --save-model

Alternatively, you can open the generated model in the FEDEM GUI and perform the
model reduction there.

To export the FMU, open the model in the GUI (and perform the model reduction,
if not already done so), and open the Model Export dialog box shown below.
You find this in the *File* menu (*File --> Export --> Export Digital Twin...*).

![FMU export](../images/fedem-fmu-export.png)

This dialog box shows three alternative ways of exporting the model,
but only the **FMU** option is relevant here. So enable that toggle.
Then use the **Browse...** button to selected the name for the fmu-file.
In the right side of the dialog, you find a list of the input- and output
indicators in the model, corresponding to the external functions and output
sensors defined in the modelling script.

Press the **Export** button to generate the fmu, and thenexit the FEDEM GUI.

## Testing the FMU

To verify that the created FMU works, you can use a tool such as
[FMPy](https://github.com/CATIA-Systems/FMPy) which also has a GUI from where
you can controll the simulation. It is also convenient to make a python script
to run it from console or to integrate with a larger simulation environment.

We here present a simple python driver, which just runs though the simulation
as it is set up in the model. The script takes the input for each time step
from a specified input file, and prints the output sensor values to the console.
Use this as a template for more advanced co-simulation tasks with FEDEM FMUs.

[Download...](linked_files/run_fedem_fmu.py)

```python
from fmpy import fmi2, read_model_description, extract
from pandas import read_csv
from sys import argv


def run(fmu_file, input_file=None, instance_name="my instance"):
    """
    Runs the specified FMU
    """
    # Read the model description
    print("Reading model description from", fmu_file)
    model = read_model_description(fmu_file)

    # Extract the FMU itself
    print("Extracting", fmu_file, "...")
    unzipdir = extract(fmu_file)

    # Setup the FMU
    print("Setup the FMU", model.coSimulation.modelIdentifier)
    fmu = fmi2.FMU2Slave(guid=model.guid, unzipDirectory=unzipdir,
                         modelIdentifier=model.coSimulation.modelIdentifier,
                         instanceName=instance_name)
    fmu.instantiate()
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    # Get some size parameters from the FMU
    num_params = fmu.getInteger([1, 2])
    num_inputs = num_params[0] # Number of input sensors
    num_output = num_params[1] # Number of output sensors

    # Read the input values into a Dataframe
    if num_inputs > 0 and input_file is not None:
        inputs = read_csv(input_file, sep="\t")

    # List of external function indices
    inpIdx = range(num_inputs)
    # List of output sensor indices
    outIdx = range(num_inputs,num_inputs+num_output)

    # Time loop, this will run through the FEDEM simulation
    # using the time domain setup in the model file used to export the FMU.
    # The two parameters to the doStep() call are dummies (time and step size).
    # They are not used in the FMU so the values are arbitrary (2*0.0 is fine).
    istep = 0
    while not fmu.getBooleanStatus(fmi2.fmi2Terminated):
        if num_inputs > 0:  # Set the external function values for this step
            fmu.setReal([*inpIdx], inputs.iloc[istep])
        fmu.doStep(0.0, 0.0)
        time = fmu.getRealStatus(fmi2.fmi2LastSuccessfulTime)
        output = fmu.getReal([*outIdx])
        istep += 1
        print(f"Here are the outputs at step={istep} time={time}:", output)

    # Finished, close down
    fmu.terminate()
    fmu.freeInstance()


if __name__ == "__main__":
    if len(argv) > 3:
        run(argv[1], argv[2], argv[3])
    elif len(argv) > 2:
        run(argv[1], argv[2])
    elif len(argv) > 1:
        run(argv[1])
    else:
        print(f"Usage: {argv[0]} <fmu-file> [<input-file>] [<instance name>]")
```
