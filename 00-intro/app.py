# %% create the point class

class Point:  # use PascalCase for classes

    """
    The Point class has public member data consisting of 2 variables,
    representing the x and y coordinates of a 2D point.
    When we create a Point object,
    we want to be able to supply the values for x and y.
    """

    # we use constructors to create the behavior Point(1,2).
    # constructors are a special method that get called when a new Point object is created.

    def __init__(self, x, y):
        """
        __init__ is a magic method that gets executed when an instance of a class is created
        """
        self.x = x
        self.y = y

    def draw(self):
        """
        draw is a function that belongs to the Point class, a method
        """
        print(f"Point ({self.x}, {self.y})")

# %% object instantiation

# what is self?? self is a reference to the current Point object,
# For example, when we call the Point object, Python will create the Point object in memory,
# and set self to reference that Point object

# self is referencing that object, and that object has a bunch of attributes and methods,
# using the "dot" operator you can see the methods, __draw__, __class__, with little square
# symbols, and attributes, __doc__, __annotations__,...
# variables that hold data about that object.
point = Point(1, 2)

# %% accessing a method

# point.x and point.y are attributes that can be printed on the terminal,
# they tell us where the point is...
print(point.x)

# %%

# we can set the self.x value to the argument or set it to 0,
# and call those methods from within the object
point.draw()

# notice, when calling the draw method, we didn't have to supply the "self" method;

# %% summary

# a class bundles data and methods into 1 unit.
# as a metaphor, think of a human, a human can have eye-color, weight etc.,
# as well as functions, like walk, talk, and eat

# %% linting

# create an instance that fails
point_fail = Point(1)
#> TypeError: Point.__init__() missing 1 required positional argument: 'y'
