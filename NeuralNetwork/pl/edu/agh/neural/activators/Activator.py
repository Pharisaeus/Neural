class Activator(object):

    def __init__(self):
        pass
    
    def should_activate(self, argument):
        raise NotImplementedError("Subclass must implement abstract method")
