# Minimum Viable Product

The product requested of us is a _derivative pricing tool_ using Monte
Carlo simulation. 
The first minimum viable product (MVP) is a simple program.
We discuss its good points, its limitations, 
and various ways around those limitations and then move to a new example. 
We continue this procedure repeatedly until we have a sophisticated tool.

## The Monte Carlo Pricing Model

### Monte Carlo Simulation

Monte Carlo simulation just means simulations that use random numbers.
Monte Carlo simulation is an extremely powerful technique, 
and there are often many problems where it is the 
only reasonable approach currently available. 
The pricing model uses random (Gaussian) numbers to simulate 
the price evolution of an asset e.g., a stock.

### The Model

The model for stock price evolution is

$$
dS_t = \mu S_t dt + \sigma S_t dW_t,
$$

where $B$ is a risk-free bond with a continuously compounding rate $r$. 
Black-Scholes pricing theory tells us the price of a vanilla option, 
with expiry $T$ and pay-off $f$, 
is equal to,

$$
e^{-rT}E\left(f(S_T)\right),
$$

where the mathematical expectation $E$ is taken 
under the associated risk-neutral process,

$$
dS_t = r S_t dt + \sigma S_t dW_t.
$$

This _stochastic differential equation_ (SDE) is solved by log-transformation and
application of Ito’s lemma, yielding:

$$
d \log(S_t) = \left(r - \frac{1}{2} \sigma^2\right) dt + \sigma dW_t.
$$

If we assume $r$ and $\sigma$ are constant, the SDE has the solution

$$
\log(S_t) = \log(S_0) + \left(r - \frac{1}{2} \sigma^2\right) t + \sigma W_t.
$$

Since $W_t$ is a Brownian motion, 
$W_T$ is distributed as a Gaussian with mean zero and variance $T$, 
so we can write

$$
W_T \sim \sqrt{T} N(0, 1),
$$

and hence

$$
\log(S_T) = \log(S_0) + \left(r - \frac{1}{2} \sigma^2\right) T + \sigma W_T,
$$

or equivalently,

$$
S_T = S_0 \cdot e^{\left(r - \frac{1}{2} \sigma^2\right) T + \sigma W_T}.
$$

The price of a vanilla option is therefore equal to

$$
e^{-rT} E\left(f\left(S_0 \cdot e^{\left(r - \frac{1}{2} \sigma^2\right) T + \sigma W_T}\right)\right)
$$

The objective of the Monte Carlo simulation is 
to approximate the expectation with the law of large numbers (LLN); 
LLN says that if $Y_j$ are a sequence of IID (identically distributed and independent) 
random variables, 
then with probability 1 the sequence,

$$
\frac{1}{N} \sum_{j=1}^{N} Y_j
$$

converges to $E(Y_1)$.

So the algorithm to price a call option by Monte Carlo is clear. 
We draw a random variable, $x$, from an $N(0,1)$ distribution and compute

$$
f\left(S_0 \cdot e^{\left(r - \frac{1}{2} \sigma^2\right) T + \sigma x}\right)
$$

where $f(S) = (S - K)^{+} = \max(0, S - K)$ is the payoff from a call option at strike price $K$. 
We do this many times and take the average. 
We then multiply this average by $e^{-rT}$ and we are done.

### Implementation

The algorithm to perform this calculation draws a random variable, 
$x$, from the Normal distribution $N(0,1)$, 
evaluates the function $f(x)$,
and computes the average after many simulations.

The code [simple_mc.py](simple_mc.py) is a minimum viable implementation of this procedure. 
It is called from [app.py](app.py).

A few points to consider,

- the script uses the base modules `math` and `random`, and the imported module [normals](normals.py)
  - `math` module is used for exponentiation, logarithms, square-roots, etc.
  - `random` is used to generate uniform r.v.s on the interval [0,1]
  - `normals` is a collection of functions for calculating Normal densities, 
  distributions, and inverse distributions
- the code pre-computes as much as possible
- the logarithm and exponential functions are avoided where possible since they are slow to compute compared to addition and multiplication

## Critiquing the Simple Monte Carlo Routine

The routine does what's needed but will soon run into difficulty when we need to add more features, 
or change a part of the simulation.
For example, 
suppose we want to perform the following modifications / enhancements 
to the current version of the model:

- change the payoff of [simple_mc.py](simple_mc.py)
- see how accurate the approximation is by adding the Monte Carlo standard error.
- improve convergence with antithetic sampling.
- calculate the most accurate estimate possible by 9am tomorrow so set it running for 14 hours.
- implement a standard error threshold to be less than 0.0001 and run it until that’s achieved. 
- add in low-discrepancy numbers and see how good they are.
- maybe standard error is a poor measure of error for low-discrepancy simulations so put in a convergence table instead.
- can we add the standard error too?
- what about changing the distribution of the generator?

If in order to change the code, 
it takes another programmer more effort to understand the routine than it does to recode it, 
he/she will recode it.
The essence then of good coding is reusability. 
Code is reusable if someone has reused it.
Reusability is as much a social concept as a technical one. 
What will make it easy for someone to reuse your code? 

Returning to the simple Monte Carlo program. 
Suppose we have to add a new feature to the routine,

- if we've designed it well, it will be easy to add new features.
- if we've designed poorly, we will have to rewrite existing code.

Given the current script, how would we add a new payoff?

Option one: 
- Copy the function, 
- change the name by adding "_another" at the end, 
- and rewrite the two lines where the condition is computed.

Option two: 
- pass in an extra parameter, possibly as a string or enum and 
- compute the boundary condition via a series of else-if statements in each loop of the Monte Carlo. 

The problem with the first option is that when we come to the next task, 
we have to adapt both the functions in the same way and do the same thing twice. 
If we then need more conditions in the future, 
this task rapidly become a maintenance nightmare. 

The issues with the second option are more subtle. 
The switch statement is an additional overhead that makes the script run a little slower. 
A deeper problem occurs if we want to use the boundary condition in another part of the code. 
We have to copy the code from inside the first routine or rewrite it as necessary. 
This again becomes a maintenance problem; 
every time we want to add some new logic, 
we have to go through every place the condition is located.

An Object-Oriented approach is to use a class. 
The class would _encapsulate_ the behavior of the payoff. 
A Condition object is then passed into the function as an argument 
and in each loop a method expressing its value is called to output the level given that condition. 