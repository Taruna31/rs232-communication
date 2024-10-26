import serial
import time
# import pandas as pd
# import csv

comport = "COM10"
baudrate = 9600


def readserial(comport, baudrate, timestamp=False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)      

    while True:

        data = ser.readline().decode().strip()

        if data and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            print(f'{timestamp} > {data}')
        elif data:
            print(data)


# def formCsvFile(headers: list[str], datas: list[str]):

#     filename = 'adam.csv'
#     with open(filename, 'w') as file:
#         for header in headers:
#             file.write(str(header)+', ')
#         file.write('n')
#         for row in datas:
#             for x in row:
#                 file.write(str(x)+', ')
#             file.write('n')

if __name__ == '__main__':
    readserial(comport, baudrate, True)                         