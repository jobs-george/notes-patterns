import random
import math

from normals import inverse_cumulative_normal


def simple_mc(the_condition, time, level, vol, drift, n_paths):
    """
    A Monte Carlo Simulation with an abstract base class Condition, 
    and polymorphic boundary-condition behavior

    """

    # the square of the coefficient of sigma * sqrt(T) * N(0,1)
    variance = vol * vol * time

    # the sqrt of above, the actual coefficient
    root_variance = math.sqrt(variance)

    # correct for stochastic derivative
    ito_correction = -0.5 * variance

    # drift part, S0 * exp(rT - 0.5*sigma^2)
    moved_level = level * math.exp(drift * time + ito_correction)

    # initialize summation
    running_sum = 0

    # do n simulations
    for i in range(n_paths):

        # get realization of standard normal r.v.
        this_gaussian = inverse_cumulative_normal(random.uniform(0, 1))

        # random part
        this_level = moved_level * math.exp(root_variance * this_gaussian)

        # boundary condition
        this_condition = the_condition(this_level)

        # add to running sum
        running_sum += this_condition

    # divide sum by # of paths
    mean = running_sum / n_paths

    # convert to martingale
    mean *= math.exp(- drift * time)

    return mean
