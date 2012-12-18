"""
Common interface for all Activator functions
"""

class Activator(object):
    """
    Common interface for all Activator functions
    """

    def calculate_response(self, argument):
        """
         Method used to calculate response of activation function for given argument
                :param argument: value that should be used as input by activation function
                :type argument: float
                :return: value calculated by activation function
                :rtype: float
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def derivative(self, argument):
        raise NotImplementedError("Subclass must implement abstract method")