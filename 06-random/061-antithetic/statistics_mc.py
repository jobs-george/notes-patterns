from abc import ABC, abstractmethod


class StatisticsMC(ABC):
    """ 
    Abstract base class for Monte Carlo Statistics

    """
    @abstractmethod
    def dump_one_result(self):
        pass

    @abstractmethod
    def get_results_so_far(self):
        pass


class StatisticsMean(StatisticsMC):
    """ 
    Class for calculating the mean of a Monte Carlo Simulation

    """

    def __init__(self):

        # declare private attributes
        self.__running_sum = 0
        self.__paths_done = 0
        self.results = [0]  # a vector for potential multiple updates

    def dump_one_result(self, result):
        self.__paths_done += 1
        self.__running_sum += result

    def get_results_so_far(self):
        self.results[0] = self.__running_sum / self.__paths_done
        return self.results
