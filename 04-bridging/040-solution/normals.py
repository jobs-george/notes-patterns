import math

one_over_root_two_pi = 0.398942280401433


def normal_density(x):
    """
    The probability density for a standard Gaussian distribution
    """
    return one_over_root_two_pi * math.exp(-x*x/2)


def inverse_cumulative_normal(u):
    """
    the Inverse Cumulative Normal function via the Beasley-Springer/Moro approximation
    """
    a = [2.50662823884,
         -18.61500062529,
         41.39119773534,
         -25.44106049637]

    b = [-8.47351093090,
         23.08336743743,
         -21.06224101826,
         3.13082909833]

    c = [0.3374754822726147,
         0.9761690190917186,
         0.1607979714918209,
         0.0276438810333863,
         0.0038405729373609,
         0.0003951896511919,
         0.0000321767881768,
         0.0000002888167364,
         0.0000003960315187]

    x = u - 0.5

    if math.fabs(x) < 0.42:  # Beasley-Springer
        y = x * x
        r = x * (((a[3] * y + a[2]) * y + a[1]) * y + a[0]) / \
            ((((b[3] * y + b[2]) * y + b[1]) * y + b[0]) * y + 1.0)
    else:
        r = u

        if x > 0:
            r = 1.0 - u

        r = math.log(-math.log(r))

        r = c[0] + r * (c[1] + r * (c[2] + r * (c[3] + r *
                                                (c[4] + r * (c[5] + r * (c[6] + r * (c[7] + r * c[8])))))))

        if x < 0:
            r = -r

    return r


def cumulative_normal(x):
    """
    The standard normal cumulative distribution function
    """
    a = [0.319381530,
         -0.356563782,
         1.781477937,
         -1.821255978,
         1.330274429]

    if x < -7.0:
        result = normal_density(x)/math.sqrt(1. + x * x)
    else:
        if x > 7.0:
            result = 1.0 - cumulative_normal(-x)
        else:
            tmp = 1.0 / (1.0 + 0.2316419 * math.fabs(x))
            result = 1 - \
                normal_density(
                    x) * (tmp * (a[0] + tmp * (a[1] + tmp * (a[2] + tmp * (a[3] + tmp * a[4])))))
            if x <= 0.0:
                result = 1.0 - result
    return result
