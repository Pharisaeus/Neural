"""
Implementation of simple network input
"""
from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Input(AbstractEdge):
    """
    Implementation of simple network input
    """

    def __init__(self, value=0):
        self.value = value

    def get_weight(self):
        """
        Method used to get weight of edge, in case of simple input it's always 1
            :rtype: float
            :return: weight of given edge
        """
        return 1.0
    
    def set_weight(self, new_weight):
        """
        Mock method - weight for simple input is always 1
            :param new_weight: new weight of given edge
            :type new_weight: float
            :rtype: None
        """
        pass

    def set_value(self, new_value):
        """
        Method used to set value of this input
                :param new_value: new value that this input should have
                :type new_value: float
                :rtype: None
                """
        self.value = new_value

    def calculate_value(self):
        """
        Method used to precalculate value of input, in case of simple input it does nothing
            :return: None
            :rtype: float
        """
        pass

    def get_value(self):
        """
        Method used to access value of input
            :return: value of input
            :rtype: float
        """
        return self.value
