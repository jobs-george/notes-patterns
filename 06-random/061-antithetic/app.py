from simple_mc import simple_mc
from condition import ConditionLower
from terminal import TerminalCondition
from parameters import ParametersConstant
from statistics_mc import StatisticsMean
from convergence_table import ConvergenceTable
from random_numbers import RandomParkMiller
from antithetic import AntiThetic

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

# Create an instance of the constant parameters
vol_param = ParametersConstant(vol)
drift_param = ParametersConstant(drift)

# Create an instance of a statistics gatherer, and decorate to convergence table
gatherer = StatisticsMean()
gatherer_table = ConvergenceTable(gatherer)

# Create an instance of a random number generator, dimension 1
generator = RandomParkMiller(1)
gen2 = AntiThetic(generator)

# Function is void, called on the statistics gatherer_table class
simple_mc(the_boundary_condition, level,
          vol_param, drift_param, n_paths, gatherer_table, gen2)

# Get the result from the gatherer object
result = gatherer_table.get_results_so_far()

# Print convergence table
fmt = "{:<10}{:<10}{}"

print(fmt.format("", "# Paths", "Levels"))
for i, (paths, levels) in enumerate(zip(result[0], result[1])):
    print(fmt.format(i, paths, levels[0]))

# compare this to the exact value of 6.33436
