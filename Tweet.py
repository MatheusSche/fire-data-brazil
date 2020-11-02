class Tweet(object):
    def __init__(self, id, len, user, userLocation, tweetText, hashtags, date, likes):
        self.__id = id
        self.__len = len
        self.__user = user
        self.__userLocation = userLocation
        self.__tweetText = tweetText
        self.__hashtags = hashtags
        self.__date = date
        self.__likes = likes

    def get_id(self):
        return self.__id

    def get_len(self):
        return self.__len

    def get_user(self):
        return self.__user

    def get_userLocation(self):
        return self.__userLocation

    def get_tweetText(self):
        return self.__tweetText

    def get_hashtags(self):
        return self.__hashtags

    def get_date(self):
        return self.__date

    def get_likes(self):
        return self.__likes
