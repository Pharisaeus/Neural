from pl.edu.agh.neural.activators.LinearActivator import LinearActivator
from pl.edu.agh.neural.activators.SigmoidActivator import SigmoidActivator
from pl.edu.agh.neural.activators.ThresholdActivator import ThresholdActivator

class ActivatorUtil(object):
    LINEAR_ACTIVATOR = LinearActivator.NAME
    SIGMOID_ACTIVATOR = SigmoidActivator.NAME
    THRESHOLD_ACTIVATOR = ThresholdActivator.NAME

    REGISTERED_ACTIVATORS = {
        LINEAR_ACTIVATOR: LinearActivator(),
        SIGMOID_ACTIVATOR: SigmoidActivator(),
        THRESHOLD_ACTIVATOR: ThresholdActivator()
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
