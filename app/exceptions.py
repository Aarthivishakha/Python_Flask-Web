class ItemNotFoundError(LookupError):
    pass


class ValidationError(ValueError):
    def __init__(self, errors: list[str]) -> None:
        super().__init__("Invalid request payload")
        self.errors = errors
