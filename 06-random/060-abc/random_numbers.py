from array import array
from normals import inverse_cumulative_normal
from abc import ABC, abstractmethod


# arrays are more efficient than lists
class RandomBase(ABC):  # The target
    """
    The random number base class has methods with set interfaces, 
    they need to be adapted to (the target) 
    """

    def __init__(self, InnerGenerator, dimensionality):

        self.__dimensionality = dimensionality
        self.inner_generator = InnerGenerator

    @abstractmethod
    def get_uniforms(self):
        pass

    @abstractmethod
    def skip(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    def get_gaussians(self, variates):

        self.inner_generator.get_uniforms(variates)

        for i in range(self.dimensionality):
            x = variates[i]
            variates[i] = inverse_cumulative_normal(x)

    @property
    def dimensionality(self):
        return self.__dimensionality


class ParkMiller(object):  # The adaptee
    """
    The Adaptee contains some useful behavior, 
    but its interface is incompatible with the existing code. 
    """

    m = 2147483647  # m = 2^31 - 1
    q = 127773  # m div a
    a = 16807
    r = 2836  # m mod a

    def __init__(self, seed=12345):

        self.__seed = seed

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, value):
        if value == 0:
            self.__seed = 1

    def max(self):
        return self.m-1

    def min(self):
        return 1

    def get_one_random_integer(self):

        hi = self.__seed / self.q
        lo = self.__seed % self.q

        test = (self.a * lo) - (self.r * hi)

        if test > 0:
            self.__seed = test
        else:
            self.__seed = test + self.m

        return self.__seed


class RandomParkMiller(RandomBase):  # The adapter
    """
    The Adapter converts the ParkMiller methods into a compatible 
    interface. 
    """

    def __init__(self, dimensionality, adaptee=ParkMiller()):
        """
        Constructor takes the ParkMiller adaptee
        """

        self.adaptee = adaptee
        self.__reciprocal = 1.0 / (1.0 + self.adaptee.max())

        self.__initial_seed = self.adaptee.seed

        super().__init__(self, dimensionality)

    def get_uniforms(self, variates):
        """
        Generate uniform r.v.s with the ParkMiller class method
        """
        for j in range(self.dimensionality):
            variates[j] = self.adaptee.get_one_random_integer() * \
                self.__reciprocal

    def skip(self, n_paths):
        tmp = array("d", [0] * self.dimensionality)
        for j in range(n_paths):
            self.get_uniforms(tmp)

    @property
    def seed(self):
        self.__seed = self.adaptee.seed
        return self.__seed

    def reset(self):
        self.adaptee = ParkMiller(self.__initial_seed)

    def reset_dimensionality(self, new_dimensionality):
        super().__init__(self, new_dimensionality)
        self.adaptee = ParkMiller(self.__initial_seed)
