from simple_mc import simple_mc
from condition import *

# Hard code inputs for now, could be a user input
time = 1/3  # yrs
boundary = 50  # boundary level
level = 55  # current level
vol = 0.1  # standard deviation
drift = 0.08  # mean drift of the process
n_paths = 10**4  # number paths to simulate


condition_types = (ConditionLower, ConditionUpper, ConditionBinary)


def condition(condition_types):  # condition_types needs to be iterable
    """ 
    Python doesn't actually care, as long as the condition method exists, 
     - if it walks like a duck, and quacks like a duck, it's probably a duck

    """
    for condition_type in condition_types:

        # individual parts need to have a condition method

        try:
            i_condition = condition_type(boundary)

            result = simple_mc(i_condition.condition, time,
                               level, vol, drift, n_paths)

            print(f"The condition {condition_type} is {result} \n")

        except:
            print("No condition method of that type")


condition(condition_types)
