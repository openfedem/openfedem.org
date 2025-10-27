"""
Simple python driver running a FEDEM FMU using the fmpy tool.

This script assumes the environment variable FEDEM_SOLVER contains the
full path to the shared object library of the FEDEM dynamics solver
(fedem_solver_core.dll on Windows, libfedem_solver_core.so on Linux).

Usage: python -m run_fedem_fmu <fmu-file> <input-file>
"""

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
    if input_file is None:
        inputs = None
    elif num_inputs > 0:
        inputs = read_csv(input_file, sep=",")

    # List of external function indices
    inpIdx = range(num_inputs)
    # List of output sensor indices
    outIdx = range(num_inputs,num_inputs+num_output)

    # Time loop, this will run through the FEDEM simulation
    # using the time domain setup of the model file used to export the FMU.
    # The two parameters to the doStep() call are dummies (time and step size).
    # They are not used in the FMU so the values are arbitrary (2*0.0 is fine).
    step = 0
    while not fmu.getBooleanStatus(fmi2.fmi2Terminated):
        if inputs is not None:  # Set external function values for next step
            # First column of inputs is not used, assuming it contains the time
            fmu.setReal([*inpIdx], inputs.iloc[step].tolist()[1:])

        fmu.doStep(0.0, 0.0)  # Advance the simulation on step

        step += 1
        time = fmu.getRealStatus(fmi2.fmi2LastSuccessfulTime)
        output = fmu.getReal([*outIdx])
        print(f"Here are the outputs at step={step} time={time}:", output)

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
