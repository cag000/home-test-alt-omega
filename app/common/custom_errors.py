class CustomError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(self.message)


class BadRequestError(CustomError):
    pass


class SuccessError(CustomError):
    pass


class InternalServerError(CustomError):
    pass


class CacheError(Exception):
    def __init__(self, message="Cache operation failed"):
        self.message = message
        super().__init__(self.message)
