from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Edge(AbstractEdge):

    def __init__(self, input_source, connection_weight):
        self.connection_weight = connection_weight
        self.input_source = input_source

    def get_weight(self):
        return self.connection_weight
    
    def set_weight(self, new_weight):
        self.connection_weight = new_weight

    def get_value(self):
        return self.input_source.get_value()
