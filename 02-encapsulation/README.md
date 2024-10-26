# Encapsulation

## Identifying classes

In the first implementation, 
wanting to add more features naturally led to classes 
that encapsulate the concept of a payoffs.
What other concepts arise naturally from the information 
we want to get from the model?

The model estimates an _expectation_, 
there are probably other statistics that could be of interest
- we could therefore abstract the notion of a 
statistic by creating a statistics gatherer class
- there are different ways to terminate a Monte Carlo simulation
  - terminate on time,
  - on standard error,
  - or simply after a fixed number of paths.
- we could abstract this by writing a terminator class.

There were many different issues with the method of random number generation. 
At the moment, 
the script relies on the base method `random` which we don't know much about. 
It would be beneficial then to have our own methods 
for random number generation. 
Another natural abstraction then is a random-number generator class.

Specifying the strike value(s) of our payoff(s) _through_ the payoff itself is fairly natural and easy.
As long as the payoff is always applied at the end of the process, 
at time $T$, 
a class that contains the condition 
and its boundary level will be neater.

More generally, 
when we pass from one problem to another problem, 
from one Monte Carlo Simulation to another, 
it will be useful if all the information about that problem were stored in one place. 
A generic `Payoff` class would know the type of payoff, 
the duration in time of the simulation, 
but wouldn't know anything about the other parameters,
the drift, 
the standard deviation, 
or the current price of the stock. 
These pieces of information should be stored in a 
booking-keeping class for example.  

The point is that by choosing a real-world concept to encapsulate, 
it is easy to decide what to include or what not to include in a class. 

## Why use classes?

Suppose that having identified all the classes, 
we implement them. 
What do we gain? 

The first gain is that the ideas that encapsulate natural concepts,
can easily used in other pieces of code. 
For example, 
suppose we have a class that performs an optimization procedure, 
used time and time again.
Not only will we save time on writing code, 
we will save time on debugging, 
since a class that has been thoroughly tested once, 
has been tested forever.
In addition, 
any quirks that evade the testing regime will be found through repeated reuse. 
The more times and ways something has been reused, 
the fewer the bugs. 

The second major gain is that the code becomes clearer. 
Having written the code in terms of natural concepts, 
another coder can identify those natural concepts, 
and pick up our code much more easily.

Finally, 
classes allow us to separate interface from implementation. 
All the user needs to know about a `Payoff` class is its strike value. 
The user doesn't need to know how that payoff is programmed.
This has multiple advantages. 
The first is that the class can be reused, 
without the programmer having to study its internal workings.
The second advantage is that because the defining characteristic of 
the class is what it does but not how it does it, 
we can change how it does it at will. 
And crucially, 
we can do this without rewriting the rest of our program. 
One aspect of this is that we can first quickly write a suboptimal implementation 
and improve it later at no cost.
This allows us to provide enough functionality 
to test the rest of the code before devoting a lot of time to the class.
A third advantage of separating interface from implementation 
is that we can write multiple classes that implement the same interface 
and use them without rewriting all the interface routines. 

## The Payoff class

Recall that we want to add another payoff to the simulation. 
The payoff is implemented as

```py
this_payoff = max(this_spot - strike, 0)
```

in the file [simple_mc.py](../01-mvp/simple_mc.py) in the MVP of the Monte Carlo simulation.

Adding another payoff might look like this 
- copy the code and add "_another" to the end of the [simple_mc.py](simple_mc.py) function, 
- or pass an extra parameter and evaluate a series of if-else statements.

Instead, 
we've identified that a `Payoff` class will be useful, 
that encapsulates the notion of a payoff. 
The file [payoff.py](payoff.py) contains the `Payoff` class. 

```py
class Payoff:

    def __init__(self, __strike, __the_payoff_type):

        # declare private attributes
        self.__the_payoff_type = __the_payoff_type
        self.__strike = __strike

    # the main method is public, we give it the strike value,
    # it returns the simulated spot at the payoff
    def payoff(self, spot):

        if self.__the_payoff_type is PayoffType.CALL:
            return max(spot - self.__strike, 0)
        elif self.__the_payoff_type is PayoffType.PUT:
            return max(self.__strike - spot, 0)
        else:
            print("unknown payoff type")

```

### Privacy

We have declared the data in the class to be private. 
This means that the data cannot be accessed by code outside the class. 
The only code that can see, 
let alone change their values, 
are the constructor `__init__` and the method `payoff`. 
Trying to access the strike from outside of the 
class will return the following exception

```py
payoff_call = Payoff(STRIKE, PayoffType.CALL)
print(payoff_call.strike)

# Traceback (most recent call last):
#   File "...>
#     print(payoff_call.strike)
# AttributeError: 'Payoff' object has no attribute 'strike'
```

What does this buy us? 
After all, 
for some reason the user might want to know the strike of a simulation, 
and we have denied them the possibility of finding out that value.

The reason is that as soon we let the user access the data directly, 
it is much harder for us to change how the class works. 
We can think of the class as a contract between coder and user. 
We the coder, have provided the user with an interface:
_if you provide a spot value we will return the payoff_. 
This is all we have contracted to provide. 
The user therefore expects and receives precisely that and no more.

For example, 
if the user could see the strike value directly and access it, 
and if we changed the class so that the strike value was no longer stored directly, 
then we would get compile errors from everywhere the strike value was accessed. 

If the class had been used in many files, 
in many different projects (which is after all the objective of code reuse), 
to find every place where the strike value had been accessed would be a daunting task. 
In fact, 
if this were the case, 
we would probably consider finding them all a considerable waste of time, 
and we would probably give up reforming the internal workings.

In other words, 
it means I can change whatever I want in the class that is private, 
without worry of breaking the rest of the code.

### Implementing the condition class

The main change from the original Monte Carlo routine is that the function [simple_mc.py](simple_mc.py) takes a payoff object as an input instead of a strike value. 
The strike value is of course now hidden inside the object.

The only line of the algorithm that is new is 

```py
this_payoff = the_payoff(this_spot)
```

The payoff object needs to be initialized with a strike value and payoff type, 
and passed a spot level like a function.
Objects that appear more like a function than 
an object are often called function objects or functors. 

We illustrate how the routine might be called in [app.py](app.py). 

```py
payoff_call = Payoff(STRIKE, PayoffType.CALL)
result_call = simple_mc(payoff_call.payoff, EXPIRY, SPOT, VOL, RATE, N_PATHS)
```

### Accessing methods / attributes in VSCode

In practice, 
the contract between code users is enforced 
through access to the methods and attributes of the class. 
Python uses dot-notation to access the attributes and methods of a class. 

An `enum` class is used to create a list of payoff types. 
Using the dot-notation, 
we see that only 2 types, `CALL` and `PUT`, are visible.
A payoff object is created given the payoff type and strike price. 
Using the dot-notation on the payoff object, 
only the payoff method is visible. 
The private methods are also visible but cannot be accessed. 
In Python, 
even private methods aren't truly private.

We have thus partially achieved our goal. 
Both call and put payoffs are called without the need to change much code. 
Adding another payoff requires updating the list of types, 
and adding the payoff code to the `Payoff` class. 
The amount of code that needs to be changed is minimal, 
but we can still do better. 
At the next checkpoint we introduce polymorphism as a more robust approach to class-based switching.

## Open-closed principle

The previous section’s discussion leads 
naturally to a programming idea known as the open-closed principle. 
Open refers to the idea that code should always be open for extension. 
So in this particular case, 
we should always be able to add extra payoffs. 

Closed means that the file is _closed for modification_. 
This refers to the idea that we should be able to do the extension 
without modifying any existing code, 
and we should be able to do so without 
even changing anything in any of the existing files. 
How can one possibly add new features without changing the `Payoff` class? 
To illustrate the idea before presenting a class-based solution, 
consider how we might do this using functions or procedural techniques. 

Suppose instead of making the class contain an enum that defines the payoff type, 
we instead use a method that points to a specific function.
The constructor for the payoff would then take in the strike value 
and the name of the function. 

This code achieves a lot of our objectives. 
We can put the function we point to in a new file, 
so the existing file for the payoff does not change each time we add a new payoff. 
This means that neither the payoff nor the Monte Carlo file needs to be changed. 

However, what do we do when the structure of the payoff changes? 
For example, suppose we want a call _and_ a put option payoff. 
This payoff requires 2 strike values, 
but we only have one parameter slot in the function chooser. 

One solution would be to use an array to specify and store parameters. 
However, 
the code is now starting to lose the properties of 
clarity and elegance which were a large part of our original objectives.
Fortunately, 
classes were introduced to solve just this sort of problem.

## Key points

We looked at one way of using a class to encapsulate the notion of a payoff. 
We then saw some of the advantages of using such a class. 
We also saw that the class had not achieved all of our requirements:
- using a `Payoff` class allows us to add extra 
forms of payoffs without modifying our Monte Carlo routine.
- by overloading we can make an object look like a function.
- the open-closed principle says that code 
should be open for extension but closed for modification
- private data helps us separate interface from implementation.