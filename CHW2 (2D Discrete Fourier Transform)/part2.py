import numpy as np
import matplotlib.pyplot as plt

f1=plt.imread("lenna256.gif")[:,:,0]
f2=plt.imread("Synth.tif")

F1=np.fft.fft2(f1)
mag1=20*np.log(np.abs(F1))
pha1=np.angle(F1)

F2=np.fft.fft2(f2)
mag2=20*np.log(np.abs(F2))
pha2=np.angle(F2)

plt.figure(1)

plt.subplot(221)
plt.imshow(mag1, cmap='gray')
plt.axis('off')
plt.title("lenna256.gif FFT magnitude")
plt.subplot(222)
plt.imshow(pha1, cmap='gray')
plt.axis('off')
plt.title("lenna256.gif FFT phase")

plt.subplot(223)
plt.imshow(mag2, cmap='gray')
plt.axis('off')
plt.title("Synth.tif FFT magnitude")
plt.subplot(224)
plt.imshow(pha2, cmap='gray')
plt.axis('off')
plt.title("Synth.tif FFT magnitude")

plt.show()