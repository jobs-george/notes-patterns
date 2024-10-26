class TerminalCondition:
    """
    The Bridge Design Pattern, a class (collection) of terminal boundary conditions

    The time parameter is unique to this collection of methods, 
    that is, the boundary conditions of these simple terminal methods are applied at the end of the measurement path

    """

    def __init__(self, __the_condition, __time):

        # private attributes
        self.__time = __time
        self.__the_condition = __the_condition

    # public methods
    def get_time(self):
        return self.__time

    def boundary_condition(self, level):
        return self.__the_condition.condition(level)
