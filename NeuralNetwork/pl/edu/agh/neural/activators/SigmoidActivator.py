from pl.edu.agh.neural.activators.Activator import Activator
from numpy.ma.core import exp

class SigmoidActivator(Activator):
    NAME = "Sigmoid Activator"

    def calculate_response(self, argument):
        return 1.0 / (1 + exp(-argument))
