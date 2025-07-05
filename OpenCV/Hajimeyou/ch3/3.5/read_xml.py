import sys
import numpy as np
import cv2

fileName = 'output.xml'

fs = cv2.FileStorage(fileName, cv2.FileStorage_READ)

if fs.isOpened is False:
    print('Failed to read file.')
    sys.exit(1)


R = fs.getNode('R_MATRIX').mat()
T = fs.getNode('T_MAT').mat()


print(R)
print(T)

fs.release()

