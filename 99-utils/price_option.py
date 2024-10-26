import math

from scipy.stats import norm


def price_option(spot, strike, expiry, r, vol, option_type="call"):
    """
    Calculate the Black-Scholes option price for a European call or put option.

    Parameters:
    spot (float): Current stock price
    strike (float): Option strike price
    expiry (float): Time to maturity in years
    r (float): Risk-free interest rate
    vol (float): Volatility of the stock
    option_type (str): "call" for call option, "put" for put option

    Returns:
    float: The Black-Scholes option price
    """
    # Calculate d1 and d2
    d1 = (math.log(spot / strike) + (r + 0.5 * vol**2) * expiry) / (
        vol * math.sqrt(expiry)
    )
    d2 = d1 - vol * math.sqrt(expiry)

    if option_type == "call":
        # Calculate call option price
        option_price = spot * norm.cdf(d1) - strike * math.exp(-r * expiry) * norm.cdf(
            d2
        )
    elif option_type == "put":
        # Calculate put option price
        option_price = strike * math.exp(-r * expiry) * norm.cdf(-d2) - spot * norm.cdf(
            -d1
        )
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price


if __name__ == "__main__":

    EXPIRY = 1 / 3  # years
    STRIKE = 50  # strike
    SPOT = 55  # current stock price
    VOL = 0.1  # volatility
    RATE = 0.08  # risk-free rate
    N_PATHS = 10**4  # number of stock price paths to simulate

    price_call = price_option(
        spot=SPOT, strike=STRIKE, expiry=EXPIRY, r=RATE, vol=VOL, option_type="call"
    )
    price_put = price_option(
        spot=SPOT, strike=STRIKE, expiry=EXPIRY, r=RATE, vol=VOL, option_type="put"
    )

    print(f"Call option price: {price_call:.5f}")
    print(f"Put option price: {price_put:.5f}")
