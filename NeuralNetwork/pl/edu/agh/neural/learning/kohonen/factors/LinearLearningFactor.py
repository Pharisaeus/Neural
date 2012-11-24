from pl.edu.agh.neural.learning.kohonen.factors.LearningFactor import LearningFactor

class LinearLearningFactor(LearningFactor):
    NAME = "Linear learning factor"

    def __init__(self, initial_value, max_iterations):
        self.initial_value = initial_value
        self.max_iterations = max_iterations

    def compute_factor(self, iteration):
        return (self.initial_value * (self.max_iterations - iteration)) / self.max_iterations