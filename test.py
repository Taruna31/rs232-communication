# test = "adam,ucok"
# index = test.index(',')

# array = [test[0:index], test[index+1:]]
# print(array)

import serial
import time

comport = "COM6"
baudrate = 9600

def readserial(comport, baudrate, timestamp=False):
    ser = serial.Serial(comport, baudrate, timeout=0.1)
    while True:
        data = ser.readline().decode().strip()
        
        if data and ',' in data:  
            index = data.index(',')
            datas = [data[0:index], data[index+1:]]

            if timestamp:
                timestamp = time.strftime('%d/%m/%Y %H:%M:%S')
                print(datas)
                result = [[timestamp, datas[0], datas[1]]]
                return result
            else:
                print(data)

def formCsvFile(headers, datas):
    filename = 'adam.csv'
    with open(filename, 'w') as file:
        file.write(', '.join(headers) + '\n')  

        for row in datas:
            file.write(', '.join(str(x) for x in row) + '\n')  

header = ['Date & Time', 'X', 'Y']

if __name__ == '__main__':
    data = readserial(comport, baudrate, True) 
    formCsvFile(header, data)  

