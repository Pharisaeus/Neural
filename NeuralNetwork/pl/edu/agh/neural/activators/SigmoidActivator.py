"""
Implementation of sigmoid (logistic) activator function
"""

from pl.edu.agh.neural.activators.Activator import Activator
from numpy.ma.core import exp

class SigmoidActivator(Activator):
    """
    Implementation of sigmoid (logistic) activator function
    """

    NAME = "Sigmoid Activator"

    def calculate_response(self, argument):
        """
         Method used to calculate response of sigmoid activation function for given argument
                :param argument: value that should be used as input by sigmoid activation function
                :type argument: float
                :return: value calculated by sigmoid activation function
                :rtype: float
        """
        return 1.0 / (1 + exp(-argument))

    def derivative(self, argument):
        if argument > 10:
            print argument
        return self.calculate_response(argument) * (1 - self.calculate_response(argument))