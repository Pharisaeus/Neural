from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Bias(AbstractEdge):

    def __init__(self, connection_weight):
        self.connection_weight = connection_weight

    def get_weight(self):
        return self.connection_weight
    
    def set_weight(self, new_weight):
        self.connection_weight = new_weight

    def get_value(self):
        return 1
