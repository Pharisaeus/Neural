from pl.edu.agh.neural.activators.Activator import Activator

class LinearActivator(Activator):
    NAME = "Linear Activator"

    def calculate_response(self, argument):
        return argument
