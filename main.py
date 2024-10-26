import serial
import time
# import pandas as pd
# import csv

comport = "COM6"
baudrate = 9600


def readserial(comport, baudrate, timestamp = False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)      

    while True:

        data = ser.readline().decode().strip()

        if data and timestamp:
            index = data.index(',')
            datas = [data[0:index], data[index+1:]]
            timestamp = time.strftime('%d/%m/%Y %H:%M:%S')
            print(datas)
            result = [[timestamp, datas[0] , datas[1]]]
            return result
        elif data:
            print(data)


def formCsvFile(headers: list[str], datas: list[str]):

    filename = 'adam.csv'
    with open(filename, 'w') as file:
        for header in headers:
            file.write(str(header)+', ')
        file.write('n')
        for row in datas:
            for x in row:
                file.write(str(x)+', ')
            file.write('n')

header = ['Date & Time', 'X', 'Y']

data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]


readserial = readserial(comport, baudrate, True) 

if __name__ == '__main__':
    # readserial(comport, baudrate, True) 
    formCsvFile(header, readserial)
    