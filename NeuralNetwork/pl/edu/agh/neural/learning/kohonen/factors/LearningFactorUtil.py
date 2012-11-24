from pl.edu.agh.neural.learning.kohonen.factors.LinearLearningFactor import LinearLearningFactor

class LearningFactorUtil(object):
    LINEAR_LEARNING_FACTOR = LinearLearningFactor.NAME

    REGISTERED_FUNCTIONS = {
        LINEAR_LEARNING_FACTOR: LinearLearningFactor
    }

    @staticmethod
    def registered_factors():
        return LearningFactorUtil.REGISTERED_FUNCTIONS.keys()

    @staticmethod
    def get_factor(name, *args):
        if name == LearningFactorUtil.LINEAR_LEARNING_FACTOR:
            return LearningFactorUtil.REGISTERED_FUNCTIONS[name](args[0], args[1])

    @staticmethod
    def default_factor():
        return LearningFactorUtil.LINEAR_LEARNING_FACTOR
