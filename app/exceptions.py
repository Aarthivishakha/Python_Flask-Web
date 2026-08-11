class ItemNotFoundError(LookupError):
    pass


class ValidationError(ValueError):
    def __init__(self, errors):
        ValueError.__init__(self, "Invalid request payload")
        self.errors = errors
