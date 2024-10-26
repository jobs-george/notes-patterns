from abc import ABC, abstractmethod


class Parameters(ABC):
    """ 
    Abstract base class for parameters, class is polymorphic, 
    takes subclass as constructor and applies mean and root_mean_square methods
    to the parameter

    """

    def __init__(self, InnerParameters):
        self.parameter = InnerParameters

    @abstractmethod
    def integral(self):
        pass

    @abstractmethod
    def integral_square(self):
        pass

    def mean(self, time1, time2):
        total = self.parameter.integral(time1, time2)
        return total/(time2 - time1)

    def root_mean_square(self, time1, time2):
        total = self.parameter.integral_square(time1, time2)
        return total/(time2 - time1)


class ParametersConstant(Parameters):
    """ 
    Constant parameter class with integral and integral_square methods

    """

    def __init__(self, constant):
        super().__init__(self)
        self.__constant = constant
        self.__constant_square = constant * constant

    def integral(self, time1, time2):
        return (time2 - time1) * self.__constant

    def integral_square(self, time1, time2):
        return (time2 - time1) * self.__constant_square
