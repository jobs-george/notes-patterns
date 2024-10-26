class Condition:
    """ 
    Parent or base class for [Boundary] Conditions

    """

    def output(self):
        print("some method")


class ConditionLower(Condition):
    """ 
    Methods for lower-absorbing boundary

    """

    def __init__(self, boundary):

        # declare private attributes
        self.__boundary = boundary

    def condition(self, level):
        return max(level - self.__boundary, 0)


class ConditionUpper(Condition):
    """ 
    Methods for upper-absorbing boundary

    """

    def __init__(self, boundary):

        # declare private attributes
        self.__boundary = boundary

    def condition(self, level):
        return max(self.__boundary - level, 0)


class ConditionBinary(Condition):
    """ 
    Converts process into a sequence of 0s and 1s

    """

    def __init__(self, boundary):

        # declare private attributes
        self.__boundary = boundary

    # wrong method name, there's no way to enforce method consistency
    def my_condition(self, level):
        return 1 if self.__boundary - level >= 0 else 0
