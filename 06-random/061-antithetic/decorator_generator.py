from random_numbers import RandomBase


class DecoratorGenerator(RandomBase):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def get_uniforms(self):
        return self._component.get_uniforms()

    def skip(self):
        return self._component.skip()

    def reset_dimensionality(self):
        return self._component.reset_dimensionality()

    def reset(self):
        return self._component.reset()
