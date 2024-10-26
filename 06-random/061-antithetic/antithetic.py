from array import array
from decorator_generator import DecoratorGenerator


class AntiThetic(DecoratorGenerator):
    """
    Decorator class that implements antithetic methods to the random number base class.
    """

    def __init__(self, component):

        super().__init__(component)

        self.__next_variates = array("d", [0] * self.dimensionality)
        self.__odd_even = True

    @property
    def dimensionality(self):
        return self.component.dimensionality

    def get_uniforms(self, variates):
        """
        Take uniforms and apply antithetic method
        """

        if self.__odd_even:

            self.component.get_uniforms(variates)

            for i in range(self.dimensionality):
                self.__next_variates[i] = 1.0 - variates[i]

            self.__odd_even = False

        else:
            variates[0] = self.__next_variates[0]

            self.__odd_even = True

    def skip(self, n_paths):

        if n_paths == 0:
            pass

        if self.__odd_even:
            self.__odd_even = False
            n_paths -= 1

        self.skip(n_paths/2)

        if n_paths % 2:
            tmp = array("d", [0] * self.dimensionality)
            self.get_uniforms(tmp)

    def reset_dimensionality(self, new_dimensionality):
        self.component.reset_dimensionality(new_dimensionality)

    def reset(self):
        self.component.reset()
        self.__odd_even = True
