class Error(object):
    def calculate_error(self, expected_output, output):
        raise NotImplementedError("Subclass must implement abstract method")