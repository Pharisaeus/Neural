from pl.edu.agh.neural.NeuronsLayer import NeuronsLayer
from pl.edu.agh.neural.learning.kohonen.KohonenLayer import KohonenLayer

class Layers(object):
    GENERAL_LAYER = NeuronsLayer.NAME
    KOHONEN_LAYER = KohonenLayer.NAME

    LAYER_TYPES = {
        GENERAL_LAYER: NeuronsLayer,
        KOHONEN_LAYER: KohonenLayer,
    }

    REVERSE_LOOKUP = dict((v, k) for k, v in LAYER_TYPES.iteritems())

    @staticmethod
    def layers_types():
        return Layers.LAYER_TYPES.keys()

    @staticmethod
    def default_layer():
        return Layers.GENERAL_LAYER

    @staticmethod
    def create_layer(layer_type):
        return Layers.LAYER_TYPES[str(layer_type)]()

    @staticmethod
    def get_type(layer):
        return Layers.REVERSE_LOOKUP[layer.__class__]