"""
Interface for all edges in network
"""
from pl.edu.agh.neural.edges.AbstractInput import AbstractInput

class AbstractEdge(AbstractInput):
    """
    Interface for all edges in network
    """

    def get_weight(self):
        """
        Method used to get weight of edge
            :rtype: float
            :return: weight of given edge
        """
        raise NotImplementedError("Subclass must implement abstract method")
    
    def set_weight(self, new_weight):
        """
        Method used to set weight of edge
            :param new_weight: new weight of given edge
            :type new_weight: float
            :rtype: None
        """
        raise NotImplementedError("Subclass must implement abstract method")

