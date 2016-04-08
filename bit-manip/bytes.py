#PYTHON 3
import struct

orig = open("video.mov", 'rb')
new = open("new.mov", 'wb')

#for b in orig.read():
for i in range(10):
  b = orig.read(1)
  i = int.from_bytes(b, byteorder='big')
  i = i + 69
  new.write(i.to_bytes(1, byteorder='big'))

orig.close()
new.close()
