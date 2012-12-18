"""
Implementation of linear activator function
"""

from pl.edu.agh.neural.activators.Activator import Activator

class LinearActivator(Activator):
    """
    Implementation of linear activator function
    """

    NAME = "Linear Activator"

    def calculate_response(self, argument):
        """
         Method used to calculate response of linear activation function for given argument
                :param argument: value that should be used as input by activation function
                :type argument: float
                :return: value calculated by activation function - in this case it will be the same as argument
                :rtype: float
        """
        return argument

    def derivative(self, argument):
        return 1