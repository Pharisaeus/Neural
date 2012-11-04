"""
Interface for all Post-synaptic-potential functions
"""
class AbstractPSP(object):
    """
    Interface for all Post-synaptic-potential functions
    """

    def calculate_potential(self, inputs):
        """
        Method used to calculate potential for given list of inputs
                :param inputs: list of AbstractInput objects
                :type inputs: list
                :return: calculated potential
                :rtype: float
        """
        raise NotImplementedError("Subclass must implement abstract method")
