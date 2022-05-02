import struct


class Unpacker:
    def __init__(self, data: bytes) -> None:
        self.offset = 0
        self.data = data

    def _unpack_struct(self, format: str):
        unpacked_data = struct.unpack_from(f'<{format}', self.data, self.offset)
        self.offset += struct.calcsize(f'<{format}')

        return unpacked_data

    def _unpack_uleb128(self):
        # https://en.wikipedia.org/wiki/LEB128 (fast-decoding)
        result = 0
        shift = 0
        while True:
            byte = self._unpack_struct('b')[0]
            result |= (byte & 0x7f) << shift
            is_last = (byte & 0x80) == 0  # is high order bit == 0
            if is_last:
                break
            shift += 7

        return result

    def unpack_byte(self):
        return self._unpack_struct('b')[0]

    def unpack_int(self):
        return self._unpack_struct('i')[0]

    def unpack_short(self):
        return self._unpack_struct('h')[0]

    def unpack_ullong(self):
        return self._unpack_struct('Q')[0]

    def unpack_string(self):
        head = self._unpack_struct('b')[0]

        if head == 0x00:
            print('no data')
            return 'no data'

        if head == 0x0b:
            length = self._unpack_uleb128()  #length(ULEB128) + string(UTF-8)
            string = self.data[self.offset:self.offset+length].decode('utf-8')
            self.offset += length

            return string


def load_file(path: str):
    with open(f'{path}', 'rb') as f:
        data = f.read()

    return data
