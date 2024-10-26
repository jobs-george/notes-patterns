from simple_mc import simple_mc


# hard-code inputs for now, could be a user input

EXPIRY = 1 / 3  # years
STRIKE = 50  # strike
SPOT = 55  # current stock price
VOL = 0.1  # volatility
RATE = 0.08  # risk-free rate
N_PATHS = 10**4  # number of stock price paths to simulate

result = simple_mc(EXPIRY, STRIKE, SPOT, VOL, RATE, N_PATHS)

print(f"The estimated call-option price is {result} \n")

# compare this to the exact value of 6.33436
