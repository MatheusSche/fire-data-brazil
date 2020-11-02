from Tweet import Tweet
from IndexName import IndexName

DADOS =[]
INDEX = []
CHUNK = 500

class ManipulateData():
    def __init__(self):
        pass

    def store_ordered_file(self, tweets_ordenados):
        for data in tweets_ordenados:
            formated_data = str(data.get_id()) + ';' + \
                            str(data.get_len()) + ';' + \
                            str(data.get_user()) + ';' + \
                            str(data.get_userLocation()) + ';' + \
                            str(data.get_tweetText()) + ';' + \
                            str(data.get_date()) + ';' + \
                            str(data.get_likes()) + '; ' + \
                            str(data.get_hashtags()) + '; '

            string_size = len(formated_data)
            formated_data += '0' * (CHUNK - string_size)
            formated_data += ';' + '\n'

            with open('twitter-data-ordered.bin', 'ab') as fileT:
                formated_data = formated_data.encode('utf-8')
                fileT.write(formated_data)

    def ordenar(self):
        twitter_data = open('twitter-data.bin', 'rb')
        twitter_data.seek(0, 2)
        tamanho = twitter_data.tell()
        twitter_data.seek(0, 0)
        position = 0
        while position < tamanho:
            line = str(twitter_data.read(502).decode('utf-8'))
            line = line.split(';')

            DADOS.append(Tweet(id=int(line[1]),
                               len=line[0],
                               user=line[2],
                               userLocation=line[3],
                               tweetText=line[4],
                               hashtags=line[7],
                               date=line[5],
                               likes=line[6]
                               )
                         )
            position += 502
            twitter_data.seek(position, 0)

        twitter_data.close()

        tweets_ordenados = sorted(DADOS, key=Tweet.get_id)
        self.store_ordered_file(tweets_ordenados)


    def store_ordered_index_name(self, index_ordenado):
        for data in index_ordenado:
            formated_data = str(data.get_user()) + ';' + \
                            str(data.get_position()) + ';'


            string_size = len(formated_data)
            formated_data += '0' * (50 - string_size)
            formated_data += ';' + '\n'

            with open('index-name-ordered.bin', 'ab') as fileT:
                formated_data = formated_data.encode('utf-8')
                fileT.write(formated_data)

    def order_index_name(self):
        users =[]
        index_name_data = open('twitter-index-name.bin', 'rb')
        index_name_data.seek(0, 2)
        tamanho = index_name_data.tell()
        index_name_data.seek(0, 0)
        position = 0

        while position < tamanho:
            line = str(index_name_data.read(52).decode('utf-8'))
            line = line.split(';')
            user = line[1]
            if user not in users:
                users.append(user)
                INDEX.append(IndexName(position=str(line[0]),
                                        user=user
                                        )
                             )
            position += 52
            index_name_data.seek(position, 0)

        index_name_data.close()

        index_ordenado = sorted(INDEX, key=IndexName.get_user)
        self.store_ordered_index_name(index_ordenado)