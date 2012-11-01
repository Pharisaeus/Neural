class AbstractInput(object):

    def get_value(self):
        raise NotImplementedError("Subclass must implement abstract method")
