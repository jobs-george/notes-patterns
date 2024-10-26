from simple_mc import simple_mc
from condition import ConditionLower
from terminal import TerminalCondition

# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate

# Create an instance of the boundary condition
the_condition = ConditionLower(boundary)
the_boundary_condition = TerminalCondition(the_condition, time)

# Pass the boundary condition into the Monte Carlo Simulation
result = simple_mc(the_boundary_condition, level, vol, drift, n_paths)

print(f"The average lower-bounded level value is {result} \n")

# compare this to the exact value of 6.33436