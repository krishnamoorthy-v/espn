class myException(Exception):
    error_msge = None
    status_code = 400

    def __init__(self, message, status_code=None, error_msge=None):
        super().__init__(message)
        self.message = message
        if status_code:
            self.status_code = status_code
        if error_msge:
            self.error_msge = error_msge

    def to_dict(self):
        response = {
            "message": self.message,
            "status_code": self.status_code
        }
        if self.error_msge is not None:
            response['error_msge'] = self.error_msge
        return response
