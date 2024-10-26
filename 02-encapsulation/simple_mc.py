import random
import math

from normals import inverse_cumulative_normal


def simple_mc(the_payoff, expiry, spot, vol, r, n_paths):
    """
    A Monte Carlo Simulation with a Payoff class
    """

    # the square of the coefficient of sigma * sqrt(T) * N(0,1)
    variance = vol * vol * expiry

    # the sqrt of above, the actual coefficient
    root_variance = math.sqrt(variance)

    # correct for stochastic derivative
    ito_correction = -0.5 * variance

    # drift part, S0 * exp(rT - 0.5*sigma^2)
    new_spot = spot * math.exp(r * expiry + ito_correction)

    # initialize summation
    running_sum = 0

    # do n simulations
    for _ in range(n_paths):

        # get realization of standard normal r.v.
        this_gaussian = inverse_cumulative_normal(random.uniform(0, 1))

        # random part
        this_spot = new_spot * math.exp(root_variance * this_gaussian)

        # payoff
        this_payoff = the_payoff(this_spot)

        # add to running sum
        running_sum += this_payoff

    # divide sum by # of paths
    mean = running_sum / n_paths

    # convert to martingale
    mean *= math.exp(-r * expiry)

    return mean
