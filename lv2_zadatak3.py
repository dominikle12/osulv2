import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road.jpg")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)

sel = img[0:200,0:300]
plt.imshow(sel)
img = np.rot90(img, -1)
plt.figure()
plt.imshow(np.fliplr(img), cmap="gray")
plt.show()