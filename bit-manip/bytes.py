#PYTHON 3
import struct
import os

orig = open("video.mov", 'rb')
new = open("new.mov", 'wb')

size = os.fstat(orig.fileno()).st_size
size = int(size/4)
for _ in range(size):
  b = orig.read(4)
  i = int.from_bytes(b, byteorder='big')
  i = i +69
  new.write(i.to_bytes(4, byteorder='big'))

orig.close()
new.close()
