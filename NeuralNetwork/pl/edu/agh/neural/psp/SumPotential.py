"""
Implementation of simple sum potential function
"""
from pl.edu.agh.neural.psp.AbstractPSP import AbstractPSP

class SumPotential(AbstractPSP):
    """
    Implementation of simple sum potential function
    """
    
    NAME = "SumPotential"

    def calculate_potential(self, inputs):
        """
        Method used to calculate potential for given list of inputs
                :param inputs: list of AbstractInput objects
                :type inputs: list
                :return: calculated potential
                :rtype: float
        """
        return self.__weighted_sum__(inputs)
    
    def __weighted_sum__(self, inputs):
        return sum([input_source.get_value() * input_source.get_weight() for input_source in inputs])
