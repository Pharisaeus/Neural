from pl.edu.agh.neural.edges.AbstractInput import AbstractInput

class AbstractEdge(AbstractInput):

    def get_weight(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def set_weight(self, new_weight):
        raise NotImplementedError("Subclass must implement abstract method")

