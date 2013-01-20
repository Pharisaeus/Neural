import math
from pl.edu.agh.neural.learning.backpropagation.error.Error import Error

class RootMeanSquare(Error):
    NAME = "Root mean square"

    def calculate_error(self, expected_output, output):
        N = len(output)
        return math.sqrt(sum([(expected_output[i] - output[i]) ** 2 for i in range(N)]) / N)