from pl.edu.agh.neural.activators.LinearActivator import LinearActivator
from pl.edu.agh.neural.activators.SigmoidActivator import SigmoidActivator

class ActivatorUtil(object):
    LINEAR_ACTIVATOR = "Linear Activator"
    SIGMOID_ACTIVATOR = "Sigmoid Activator"

    REGISTERED_ACTIVATORS = {
        LINEAR_ACTIVATOR: LinearActivator(),
        SIGMOID_ACTIVATOR: SigmoidActivator()
    }

    @staticmethod
    def registered_activators():
        return ActivatorUtil.REGISTERED_ACTIVATORS.keys()

    @staticmethod
    def get_activator(name):
        return ActivatorUtil.REGISTERED_ACTIVATORS[name]

    @staticmethod
    def default_activator():
        return ActivatorUtil.LINEAR_ACTIVATOR
