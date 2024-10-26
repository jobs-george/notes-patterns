from simple_mc import simple_mc
from condition import Condition, ConditionBinary

# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate

# With pylint, we get an error - Abstract method instantiated
condition = Condition()

# Get another error because ConditionBinary doesn't have the condition method
binary_result = ConditionBinary(100)
