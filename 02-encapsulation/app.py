from simple_mc import simple_mc
from payoff import PayoffType, Payoff

# hard-code inputs for now, could be a user input

EXPIRY = 1 / 3  # years
STRIKE = 50  # strike
SPOT = 55  # current stock price
VOL = 0.1  # volatility
RATE = 0.08  # risk-free rate
N_PATHS = 10**4  # number of stock price paths to simulate

# create the lower and upper payoffs
payoff_call = Payoff(STRIKE, PayoffType.CALL)
payoff_put = Payoff(STRIKE, PayoffType.PUT)

result_call = simple_mc(payoff_call.payoff, EXPIRY, SPOT, VOL, RATE, N_PATHS)
result_put = simple_mc(payoff_put.payoff, EXPIRY, SPOT, VOL, RATE, N_PATHS)

print(f"The estimated call-option price is {result_call} \n")
print(f"The estimated put-option price is {result_put} \n")

# compare this to the exact values of 6.33436 and 0.018650
