from decorator_statistics import DecoratorStatistics


class ConvergenceTable(DecoratorStatistics):
    """
    Concrete Decorators call the wrapped object and alter its result in some way.
    """

    def __init__(self, component):

        super().__init__(component)

        # declare private attributes
        self.__stopping_point = 2
        self.__paths_done = 0
        self.this_result = [[], []]

    def dump_one_result(self, result):
        """
        Decorators can call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """

        self.component.dump_one_result(result)
        self.__paths_done += 1

        if self.__paths_done == self.__stopping_point:

            self.__stopping_point *= 2
            self.this_result[0].append(self.__paths_done)
            self.this_result[1].append(
                tuple(self.component.get_results_so_far()))  # See Appendix

    def get_results_so_far(self):
        """
        Another decorated method
        """

        if self.__paths_done * 2 != self.__stopping_point:  # get the last value if it's there
            self.this_result[0].append(self.__paths_done)
            self.this_result[1].append(
                tuple(self.component.get_results_so_far()))

        return self.this_result
