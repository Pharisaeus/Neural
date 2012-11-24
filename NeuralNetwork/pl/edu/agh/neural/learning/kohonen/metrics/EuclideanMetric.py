import numpy
from pl.edu.agh.neural.learning.kohonen.metrics.Metric import Metric

class EuclideanMetric(Metric):
    NAME = "Euclidean Metric"

    def compute_distance(self, a, b):
        return numpy.linalg.norm(numpy.array(a) - numpy.array(b))