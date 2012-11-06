"""
Implementation of threshold (steep sigmoid) activator function
"""

from pl.edu.agh.neural.activators.Activator import Activator
from numpy.ma.core import exp

class ThresholdActivator(Activator):
    """
    Implementation of threshold (steep sigmoid) activator function
    """

    NAME = "Threshold Activator"

    def calculate_response(self, argument):
        """
         Method used to calculate response of threshold activation function for given argument
                :param argument: value that should be used as input by threshold activation function
                :type argument: float
                :return: value calculated by threshold activation function
                :rtype: float
        """
        return 1.0 / (1 + exp(-1000 * argument))
