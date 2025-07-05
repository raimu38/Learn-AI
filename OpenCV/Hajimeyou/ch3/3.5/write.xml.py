import numpy as np
import cv2

filename = "output.xml"

fs = cv2.FileStorage(filename, cv2.FileStorage_WRITE)

if fs.isOpened() is False:
    print("Failed to load XML file.")
    sys.exit(1)

R = np.eye(4,3)
T = np.zeros((3,1))

fs.write('R_MATRIX', R)
fs.write('T_MAT', T)

fs.writeComment('This is comment')

fs.release()
