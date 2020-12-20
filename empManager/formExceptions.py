class formFieldException(Exception):
    def __init__(self, errors,  message="",):
        super().__init__(message)

        self.errors = errors

