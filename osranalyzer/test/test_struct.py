import struct

while True:
    format = input('format 입력: ')
    print(struct.calcsize(format))