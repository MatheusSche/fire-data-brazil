class Functions():

    def __init__(self):
        pass

    def binarySearch_it(self, key):
        arq_b = open('twitter-data-ordered.bin', 'rb')
        arq_b.seek(0, 2)
        length = arq_b.tell()

        left = 0
        right = length - 502
        arq_b.seek(0, 0)
        while (left <= right):

            middle = int((left + right) // 2)
            while middle % 502 != 0:
                middle = middle - 1
            arq_b.seek(middle, 0)
            valor = arq_b.read(502).decode('utf-8')
            valor = str(valor)
            valor = valor.split(';')
            id = int(valor[0])
            print('Comparando {} --- {}'.format(id, key))
            if int(id) == int(key):
                print(middle, 'Encontrou')
                break
            elif int(key) > int(id):
                left = middle + 502
            elif int(key) < int(id):
                right = middle - 502
        else:
            print("Value not found")

        arq_b.close()

    def show_all_registers(self):
        twitter_data = open('twitter-data-ordered.bin', 'rb')

        twitter_data.seek(0, 2)
        tamanho = twitter_data.tell()

        twitter_data.seek(0, 0)
        position = 0

        while position < tamanho:
            line = str(twitter_data.read(502))
            print(line)
            position += 502

        twitter_data.close()

    def binarySearch_it_index_id(self, key):

        index_data = open('twitter-index-id.bin', 'rb')

        index_data.seek(0, 2)
        tamanho_index = index_data.tell()

        index_data.seek(0, 0)
        position_index = 0

        last_position = 0
        last_id = 0
        flag = 0

        while position_index < tamanho_index:
            line = str(index_data.read(52).decode('utf-8'))
            line = line.split(';')
            current_position = int(line[0])
            current_id = str(line[1])

            if key > current_id:
                last_position = current_position
                last_id = current_id

                position_index += 52
            else:
                begin = last_position
                end = current_position
                flag = 1
                break

        index_data.close()

        if flag == 0:
            return 0

        arq_b = open('twitter-data-ordered.bin', 'rb')
        arq_b.seek(0, 2)
        length = arq_b.tell()

        left = begin
        right = end
        arq_b.seek(0, 0)
        while (left <= right):

            middle = int((left + right) // 2)
            while middle % 502 != 0:
                middle = middle - 1
            arq_b.seek(middle, 0)
            valor = arq_b.read(502).decode('utf-8')
            valor = str(valor)
            valor = valor.split(';')
            id = int(valor[0])
            print('Comparando {} --- {}'.format(id, key))
            if int(id) == int(key):
                print(middle, 'Encontrou')
                break
            elif int(key) > int(id):
                left = middle + 502
            elif int(key) < int(id):
                right = middle - 502
        else:
            print("Value not found")

        arq_b.close()

    def create_index_file_by_id(self):
        twitter_data = open('twitter-data-ordered.bin', 'rb')

        twitter_data.seek(0, 2)
        tamanho = twitter_data.tell()

        twitter_data.seek(0, 0)
        position = 0

        while position < tamanho:
            print(position, tamanho)
            twitter_data.seek(position, 0)
            line = str(twitter_data.read(502).decode('utf-8'))
            line = line.split(';')
            id = line[0]
            register = ''
            register += str(position) + ';' + str(id) + ';'

            string_size = len(register)
            register += '0' * (50 - string_size)
            register += ';' + '\n'

            with open('twitter-index-id.bin', 'ab') as twitter_index:
                register = register.encode('utf-8')
                twitter_index.write(register)

            position += (502 * 500)

        twitter_data.close()

    def create_index_file(self):
        twitter_data = open('twitter-data-ordered.bin', 'rb')

        twitter_data.seek(0, 2)
        tamanho = twitter_data.tell()

        twitter_data.seek(0, 0)
        position = 0

        while position < tamanho:
            line = str(twitter_data.read(502).decode('utf-8'))
            line = line.split(';')
            id = line[0]
            register = ''
            register += str(position) + ';' + str(id) + ';'

            string_size = len(register)
            register += '0' * (50 - string_size)
            register += ';' + '\n'

            with open('twitter-index.bin', 'ab') as twitter_index:
                register = register.encode('utf-8')
                twitter_index.write(register)


            position += 502

        twitter_data.close()

    def crete_index_by_name(self):
        twitter_data = open('twitter-data-ordered.bin', 'rb')

        twitter_data.seek(0, 2)
        tamanho = twitter_data.tell()

        twitter_data.seek(0, 0)
        position = 0

        while position < tamanho:
            line = str(twitter_data.read(502).decode('utf-8'))
            line = line.split(';')
            user = line[2]
            register = ''
            register += str(position) + ';' + str(user) + ';'

            string_size = len(register)
            register += '0' * (50 - string_size)
            register += ';' + '\n'

            with open('twitter-index-name.bin', 'ab') as twitter_index:
                register = register.encode('utf-8')
                twitter_index.write(register)

            position += 502

        twitter_data.close()

    def direct_in_data(self, position):
        data_file = open('twitter-data-ordered.bin', 'rb')
        data_file.seek(position)
        valor = data_file.read(502)
        print(valor)
        data_file.close()

    def binarySearch_it_ID(self, key):
        arq_b = open('twitter-index.bin', 'rb')
        arq_b.seek(0, 2)
        length = arq_b.tell()

        left = 0
        right = length - 52
        arq_b.seek(0, 0)
        while (left <= right):

            middle = int((left + right) // 2)
            while middle % 52 != 0:
                middle = middle - 1
            arq_b.seek(middle, 0)
            valor = arq_b.read(52).decode('utf-8')
            valor = str(valor)
            valor = valor.split(';')
            id = valor[1]

            print('Comparando {} --- {}'.format(id, key))
            if int(id) == int(key):
                position = int(valor[0])
                print(middle, 'Encontrou')
                print("Acessando o arquivo de dados")
                print()
                self.direct_in_data(position=position)
                break
            elif int(key) > int(id):
                left = middle + 52
            elif int(key) < int(id):
                right = middle - 52
        else:
            print("Value not found")

        arq_b.close()


    def binarySearch_USER(self, key):
        arq_b = open('index-name-ordered.bin', 'rb')
        arq_b.seek(0, 2)
        length = arq_b.tell()

        left = 0
        right = length - 52
        arq_b.seek(0, 0)
        while (left <= right):

            middle = int((left + right) // 2)
            while middle % 52 != 0:
                middle = middle - 1
            arq_b.seek(middle, 0)
            valor = arq_b.read(52).decode('utf-8')
            valor = str(valor)
            valor = valor.split(';')
            user = str(valor[0])

            print('Comparando {} --- {}'.format(user, key))
            if user == key:
                position = int(valor[1])
                print(middle, 'Encontrou')
                print("Acessando o arquivo de dados")
                print()
                self.direct_in_data(position=position)
                break
            elif key > user:
                left = middle + 52
            elif key < user:
                right = middle - 52
        else:
            print("Value not found")

        arq_b.close()

    def answare_hypothesis(self):
        key_words_dict = {
            'gado': 0,
            'boi': 0,
            'pasto': 0,
            'criminoso': 0,
            '#forasalles': 0,
            'aquecimento global': 0,
            'acao humana': 0,
            'acidente': 0,
            'acidental': 0,
            'seca': 0,
            'pantanal': 0,
            'amazonia': 0
        }
        key_words = ['gado',
                     'boi',
                     'pasto',
                     'criminoso',
                     '#forasalles',
                     'aquecimento global',
                     'acao humana',
                     'acidente',
                     'seca',
                     'acidental',
                     'pantanal',
                     'amazonia'
                     ]

        for word in key_words:
            twitter_data = open('twitter-data-ordered.bin', 'rb')

            twitter_data.seek(0, 2)
            tamanho = twitter_data.tell()

            twitter_data.seek(0, 0)
            position = 0
            cont = 0

            while position < tamanho:
                line = str(twitter_data.read(502))
                line = line.split(';')
                texto = line[4].lower()
                if word in texto:
                    cont += texto.count(word)
                position += 502

            twitter_data.close()

            key_words_dict[word] = cont

        return key_words_dict
