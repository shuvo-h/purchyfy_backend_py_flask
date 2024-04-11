class AppError(Exception):
    def __init__(self, status_code,message,errors=None):
        self.status_code = status_code
        self.message = message
        self.errors = errors
        super().__init__(message)
