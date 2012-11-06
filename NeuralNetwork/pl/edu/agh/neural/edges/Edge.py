"""
Implementation of simple network edge
"""
from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Edge(AbstractEdge):
    """
    Implementation of simple network edge
        :param input_source: input source for this edge (should provide value)
        :type input_source: AbstractInput
        :param connection_weight: weight of connection with given input
        :type connection_weight: float
    """

    def __init__(self, input_source, connection_weight):
        self.connection_weight = connection_weight
        self.input_source = input_source

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
        Method used to precalculate value of input, in case of edge it delgates call to connected neuron
            :return: None
            :rtype: float
        """
        self.input_source.calculate_value()

    def get_value(self):
        """
        Method used to access value of input
            :return: value of input
            :rtype: float
        """
        return self.input_source.get_value()
