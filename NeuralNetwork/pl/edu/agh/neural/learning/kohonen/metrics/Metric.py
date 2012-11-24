class Metric(object):
    def compute_distance(self, a, b):
        raise NotImplementedError("Subclass must implement abstract method")
