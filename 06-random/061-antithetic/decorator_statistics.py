from statistics_mc import StatisticsMC


class DecoratorStatistics(StatisticsMC):
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

    def dump_one_result(self):
        return self._component.dump_one_result()

    def get_results_so_far(self):
        return self._component.get_results_so_far()
