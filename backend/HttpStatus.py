class Status:
    def __init__(self) -> None:
        None

    @staticmethod
    def ok() -> int:
        return 200
    
    @staticmethod
    def bad_request() -> int:
        return 400
