from pl.edu.agh.neural.Layers import Layers
from pl.edu.agh.neural.learning.cp.gui.CounterPropagationLearningDialog import CounterPropagationLearningDialog
from pl.edu.agh.neural.learning.kohonen.gui.KohonenLearningDialog import KohonenLearningDialog

class LearningLauncher(object):
    @staticmethod
    def dialog(network):
        layers = network.get_layers()
        if Layers.get_type(layers[0]) == Layers.KOHONEN_LAYER:
            if len(layers) == 2 and Layers.get_type(layers[1]) == Layers.GENERAL_LAYER:
                return CounterPropagationLearningDialog(network)
            else:
                return KohonenLearningDialog(network)
