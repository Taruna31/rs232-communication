import serial
import time

comport = "COM6"
baudrate = 9600
filename = 'adam.csv'

def readserial(comport, baudrate, filename, timestamp=False):
    ser = serial.Serial(comport, baudrate, timeout=0.1)

    with open(filename, 'a') as file:
        if file.tell() == 0:  
            headers = ['Date & Time', 'X', 'Y']
            file.write(', '.join(headers) + '\n')

        while True:
            data = ser.readline().decode().strip()
            
            if data and ',' in data:  
                index = data.index(',')
                datas = [data[0:index], data[index+1:]]
                
                
                if timestamp:
                    timestamp_str = time.strftime('%d/%m/%Y %H:%M:%S')
                    row = [timestamp_str, datas[0], datas[1]]
                else:
                    row = [datas[0], datas[1]]

               
                file.write(', '.join(row) + '\n')
                print("Data saved to CSV:", row)

                file.flush()

if __name__ == '__main__':
    readserial(comport, baudrate, filename, True)
