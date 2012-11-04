"""
Implementation of bias input
"""
from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Bias(AbstractEdge):
    """
    Implementation of bias input
    """

    def __init__(self, connection_weight):
        self.connection_weight = connection_weight

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

    def get_value(self):
        """
        Method used to access value of input
            :return: value of input
            :rtype: float
        """
        return 1.0
