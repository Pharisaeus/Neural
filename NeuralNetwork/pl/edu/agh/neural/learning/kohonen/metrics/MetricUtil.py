from pl.edu.agh.neural.learning.kohonen.metrics.EuclideanMetric import EuclideanMetric

class MetricUtil(object):
    EUCLIDEAN_METRIC = EuclideanMetric.NAME

    REGISTERED_METRICS = {
        EUCLIDEAN_METRIC: EuclideanMetric
    }

    @staticmethod
    def registered_metrics():
        return MetricUtil.REGISTERED_METRICS.keys()

    @staticmethod
    def get_metric(name):
        return MetricUtil.REGISTERED_METRICS[name]

    @staticmethod
    def default_metric():
        return MetricUtil.EUCLIDEAN_METRIC