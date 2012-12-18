import numpy

class DataNormalizer(object):
    @staticmethod
    def normalize(data):
        result = []
        for v in data:
            norm = numpy.linalg.norm(v)
            result.append(v / norm if norm > 0 else v)
        return result