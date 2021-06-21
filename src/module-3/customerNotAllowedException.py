

class CustomerNotAllowedException(Exception):

    def __init__(self,message):
        self.message="Customer "+message+" Not Allowed.\n"
