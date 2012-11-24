from pl.edu.agh.neural.learning.kohonen.neighbourhood.GaussianNeighbourhoodFunction import GaussianNeighbourhoodFunction

class NeighbourhoodUtil(object):
    GAUSSIAN_NEIGHBOURHOOD = GaussianNeighbourhoodFunction.NAME

    REGISTERED_FUNCTIONS = {
        GAUSSIAN_NEIGHBOURHOOD: GaussianNeighbourhoodFunction,
    }

    @staticmethod
    def registered_neighbourhoods():
        return NeighbourhoodUtil.REGISTERED_FUNCTIONS.keys()

    @staticmethod
    def get_neighbourhood(name):
        return NeighbourhoodUtil.REGISTERED_FUNCTIONS[name]

    @staticmethod
    def default_neighbourhood():
        return NeighbourhoodUtil.GAUSSIAN_NEIGHBOURHOOD
