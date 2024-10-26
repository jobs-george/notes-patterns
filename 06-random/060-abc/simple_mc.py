from array import array
import math


def simple_mc(the_boundary_condition, level, vol, drift, n_paths, gatherer, generator):
    """
    A Monte Carlo Simulation with an abstract base class Condition, 
    polymorphic boundary-condition behavior,
    and an encapsulated time parameter.

    Parameters are time-dependent or stochastic extensible

    Simulation book-keeping is done by the statistics or convergence table gatherer

    Random number generator class

    """

    # reset dimensionality
    generator.reset_dimensionality(1)

    # get the time parameter
    time = the_boundary_condition.time

    # the square of the coefficient of sigma * sqrt(T) * N(0,1)
    variance = vol.integral_square(0, time)

    # the sqrt of above, the actual coefficient
    root_variance = math.sqrt(variance)

    # correct for stochastic derivative
    ito_correction = -0.5 * variance

    # drift part, S0 * exp(rT - 0.5*sigma^2)
    moved_level = level * math.exp(drift.integral(0, time) + ito_correction)

    # Calculate log-normal drift
    rescaling = math.exp(- drift.integral(0, time))

    # Initialise variate array
    variate_array = array("f", [0] * generator.dimensionality)

    # do n simulations
    for i in range(n_paths):

        # get realization of standard normal r.v.
        generator.get_gaussians(variate_array)

        # random part
        this_level = moved_level * math.exp(root_variance * variate_array[0])

        # boundary condition
        this_condition = the_boundary_condition.boundary_condition(this_level)

        # Results accounting
        gatherer.dump_one_result(this_condition * rescaling)
