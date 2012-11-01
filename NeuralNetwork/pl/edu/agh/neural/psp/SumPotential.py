from pl.edu.agh.neural.psp.AbstractPSP import AbstractPSP

class SumPotential(AbstractPSP):

    def calculate_potential(self, inputs):
        return self.__weighted_sum__(inputs)
    
    def __weighted_sum__(self, inputs):
        return sum([input_source.get_value() * input_source.get_weight() for input_source in inputs])
