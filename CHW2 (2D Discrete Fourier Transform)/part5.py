import numpy as np
import matplotlib.pyplot as plt

f1=plt.imread("lenna256.gif")[:,:,0]
f2=plt.imread("Synth.tif")

fil1=f1.copy()
fil2=f2.copy()

F1=np.fft.fft2(fil1)
mag1=20*np.log(np.abs(F1))
pha1=np.angle(F1)

F2=np.fft.fft2(fil2)
mag2=20*np.log(np.abs(F2))
pha2=np.angle(F2)

plt.figure(1)

plt.subplot(221)
plt.imshow(f2, cmap='gray')
plt.axis('off')
plt.title("Synth")

plt.subplot(222)
plt.imshow(f1, cmap='gray')
plt.axis('off')
plt.title("Lenna")

plt.subplot(223)
F1=np.abs(F1)*np.exp(1j*pha2)
f1=np.fft.ifft2(F1)
f1=np.abs(f1)
plt.imshow(f1, cmap='gray')
plt.axis('off')
plt.title("Lenna < Circle")

plt.subplot(224)
F2=np.abs(F2)*np.exp(1j*pha1)
f2=np.fft.ifft2(F2)
f2=np.abs(f2)
plt.imshow(f2, cmap='gray')
plt.axis('off')
plt.title("Circle < Lenna")

plt.show()