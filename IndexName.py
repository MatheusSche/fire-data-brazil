class IndexName(object):
    def __init__(self, position, user):
        self.__position = position
        self.__user = user


    def get_position(self):
        return self.__position

    def get_user(self):
        return self.__user

