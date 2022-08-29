import random
import threading as th
from datetime import datetime

status = {'ENCODED': [0, 0], 'FILESIZE': 0}

class Encode:
    encoded = []

    @staticmethod
    def generateTable(seed):
        random.seed(seed)
        table = [i for i in range(256)]
        random.shuffle(table)
        return table

    @staticmethod
    def encode(table, data):
        status['ENCODED'][1] = len(data)
        for i, byte in enumerate(data):
            Encode.encoded.append(table[byte])
            status['ENCODED'][0] = i

class Decode:
    decoded = []

    @staticmethod
    def generateTable(seed):
        random.seed(seed)
        table = [i for i in range(256)]
        random.shuffle(table)
        decTable = [i for i in range(256)]
        for i, val in enumerate(table):
            decTable[val] = i
        return decTable

    @staticmethod
    def decode(table, data):
        status['ENCODED'][1] = len(data)
        for i, byte in enumerate(data):
            Decode.decoded.append(table[byte])
            status['ENCODED'][0] = i


def writeInFile(filename, data):
    with open(filename, 'wb') as file:
        file.write(bytearray(data))

def fileOpen(filename):
    try:
        with open(filename, 'rb') as file:
            data = tuple(file.read())
            status['FILESIZE'] = len(data)
            return data
    except FileNotFoundError:
        input('ERROR: File not found! Press any key to exit...')
        exit()

def encode():
    print('Encoding mode')
    file_IN = input('Enter file name: ')
    key = int(input('Enter key: '))

    startTime = datetime.now()
    print('File opening... ', end='')
    filedata = fileOpen(file_IN)
    print('[DONE]')

    print('Generating encoding table... ', end='')
    table = Encode.generateTable(key)
    print('[DONE]')

    thr = th.Thread(target=Encode.encode, args=(table, filedata,))
    print('\rEncoding... ', end='')
    thr.start()
    while thr.is_alive():
        print(f'\rEncoding... {status["ENCODED"][0]}/{status["ENCODED"][1]}', end='')
    print(f'\rEncoding... {status["ENCODED"][1]}/{status["ENCODED"][1]} [DONE]\n', end='')
    del filedata
    end_time = datetime.now() - startTime

    file_OUT = input('Enter out file name: ')
    print('Writing... ', end='')
    writeInFile(file_OUT, Encode.encoded)
    print('[DONE]')
    Encode.encoded.clear()

    input(f"""============ INFO ============
    Input file: {file_IN}
    Output file: {file_OUT}
    File size: {round(status['FILESIZE'] / 1024, 1)} KiB
    Key: {key}
    Encoding table: {' | '.join(map(str, [f'{i} -> {j}' for i, j in enumerate(table)]))}
    Elapsed time: {end_time}
    """)

def decode():
    print('Decoding mode')
    file_IN = input('Enter file name: ')
    key = int(input('Enter key: '))

    startTime = datetime.now()
    print('File opening... ', end='')
    filedata = fileOpen(file_IN)
    print('[DONE]')

    print('Generating decoding table... ', end='')
    table = Decode.generateTable(key)
    print('[DONE]')

    thr = th.Thread(target=Decode.decode, args=(table, filedata,))
    print('\rDecoding... ', end='')
    thr.start()
    while thr.is_alive():
        print(f'\rDecoding... {status["ENCODED"][0]}/{status["ENCODED"][1]}', end='')
    print(f'\rDecoding... {status["ENCODED"][1]}/{status["ENCODED"][1]} [DONE]\n', end='')
    del filedata
    end_time = datetime.now() - startTime

    file_OUT = input('Enter out file name: ')
    print('Writing... ', end='')
    writeInFile(file_OUT, Decode.decoded)
    print('[DONE]')
    Decode.decoded.clear()

    input(f"""============ INFO ============
    Input file: {file_IN}
    Output file: {file_OUT}
    File size: {round(status['FILESIZE'] / 1024, 1)} KiB
    Key: {key}
    Decoding table: {' | '.join(map(str, [f'{i} -> {j}' for i, j in enumerate(table)]))}
    Elapsed time: {end_time}
    """)

q = input('Select mode (encoding/decoding) [e/d]: ')

match q:
    case 'e': encode()
    case 'd': decode()


# my code is a piece of shit, my inglish too 