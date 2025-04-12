import numpy as np

import  cv2

img = np.array([[1,1,3,0,1,0,0,1,0]])

count = cv2.countNonZero(img)
print(f"count: {count}")
