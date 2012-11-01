from pl.edu.agh.neural.edges.AbstractEdge import AbstractEdge

class Input(AbstractEdge):

    def __init__(self, value=0):
        self.value = value

    def get_weight(self):
        return 1
    
    def set_weight(self, new_weight):
        pass

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value
