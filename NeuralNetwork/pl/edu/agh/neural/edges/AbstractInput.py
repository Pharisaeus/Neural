"""
Interface for all neuron inputs
"""
class AbstractInput(object):
    """
    Interface for all neuron inputs
    """

    def calculate_value(self):
        """
        Method used to precalculate value of input
            :return: None
            :rtype: float
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def get_value(self):
        """
        Method used to access value of input
            :return: value of input
            :rtype: float
        """
        raise NotImplementedError("Subclass must implement abstract method")
