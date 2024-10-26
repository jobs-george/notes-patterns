from enum import Enum, auto


class PayoffType(Enum):
    """ 
    Enum class for listing the types of payoff 
    """
    CALL = auto()
    PUT = auto()


class Payoff:
    """ 
    class for storing payoff information
    """

    def __init__(self, __strike, __the_payoff_type):
        """ 
        The constructor for the Payoff class. 

        Parameters:
            strike (private): The level the strike is set at.
            the_payoff_type (private): the payoff, e.g., call or put

        """

        # declare private attributes
        self.__the_payoff_type = __the_payoff_type
        self.__strike = __strike

    # the main method is public, we give it the strike value,
    # it returns the simulated spot at the payoff
    def payoff(self, spot):
        """ 
        Given the payoff type, switches payoff method. 

        Parameters: 
            spot: The current price of the stock. 

        Returns: 
            The spot level given the payoff
        """
        if self.__the_payoff_type is PayoffType.CALL:
            return max(spot - self.__strike, 0)
        elif self.__the_payoff_type is PayoffType.PUT:
            return max(self.__strike - spot, 0)
        else:
            print("unknown payoff type")
