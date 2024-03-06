class InvalidOperationError(Exception):
    def __init__(self, message="Invalid operation"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
