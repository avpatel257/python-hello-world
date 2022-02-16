from msilib.schema import Class
from unicodedata import name


class Session:
    """ Session Class """

    # class variable shared by all instances
    kind = 'session'         

    def __init__(self, name, sessionId):
        # instance variable unique to each instance
        self.name = name 
        self.sessionId = sessionId

    def is_session_valid():
        return True