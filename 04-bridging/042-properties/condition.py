from abc import ABC, abstractmethod


class Condition(ABC):
    """ 
    Abstract base class for [Boundary] Conditions

    """

    @abstractmethod
    def condition(self):
        """ 
        All subclasses must have a condition method

        """
        pass


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
    Converts process into a sequence of 0s and 1s, bounded above

    """

    def __init__(self, boundary):

        # declare private attributes
        self.__boundary = boundary

    def condition(self, level):
        return 1 if self.__boundary - level >= 0 else 0


class ConditionDoubleBinary(Condition):
    """ 
    Converts process into a sequence of 0s and 1s, bounded above and below

    """

    def __init__(self, lower, upper):

        # declare private attributes
        self.__lower = lower
        self.__upper = upper

    def condition(self, level):
        if level <= self.__lower:
            return 0
        elif level >= self.__upper:
            return 0
        return 1
