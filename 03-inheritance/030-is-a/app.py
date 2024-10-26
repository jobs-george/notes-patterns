from simple_mc import simple_mc
from condition import Condition, ConditionBinary

# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate

# We shouldn't be able to directly access the Condition class here,
# it's an abstract class that lets us create logic for subclasses
condition = Condition()

# Get another error because ConditionBinary doesn't contain the condition method
binary_condition = ConditionBinary(boundary)

# Binary method should be "condition" not "my_condition"
result_binary = simple_mc(binary_condition.condition,
                          time, level, vol, drift, n_paths)

print(f"The average upper-bounded binary-level value is {result_binary} \n")

# Abstract base classes (ABCs) solve this problem
