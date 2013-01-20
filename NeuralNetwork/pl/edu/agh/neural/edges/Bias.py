"""
Implementation of bias input
"""
from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Bias(AbstractEdge):
    """
    Implementation of bias input
        :param connection_weight: weight of bias connection (value is always 1)
        :type connection_weight: float
    """

    def __init__(self, connection_weight):
        self.connection_weight = connection_weight
        self.value = -1.0

    def get_weight(self):
        """
        Method used to get weight of edge
            :rtype: float
            :return: weight of given edge
        """
        return self.connection_weight
    
    def set_weight(self, new_weight):
        """
        Method used to set weight of edge
            :param new_weight: new weight of given edge
            :type new_weight: float
            :rtype: None
        """
        self.connection_weight = new_weight

    def calculate_value(self):
        """
        Method used to precalculate value of input, in case of bias it does nothing
            :return: None
            :rtype: float
        """
        pass

    def get_value(self):
        """
        Method used to access value of input, in case of bias it's always 1
            :return: value of input
            :rtype: float
        """
        return self.value

    def enable(self):
        self.value=-1.0

    def disable(self):
        self.value=0.0
