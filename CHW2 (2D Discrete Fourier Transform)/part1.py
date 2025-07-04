import numpy as np
import matplotlib.pyplot as plt

f1=plt.imread("lenna256.gif")[:,:,0]
f2=plt.imread("Synth.tif")

plt.figure(1)

plt.subplot(121)
plt.imshow(f1, cmap='gray')
plt.axis('off')
plt.subplot(122)
plt.imshow(f2, cmap='gray')
plt.axis('off')

plt.show()