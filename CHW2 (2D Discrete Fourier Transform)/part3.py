import numpy as np
import matplotlib.pyplot as plt

f1=plt.imread("lenna256.gif")[:,:,0]
f2=plt.imread("Synth.tif")

fil1=f1.copy()
fil2=f2.copy()

for i in np.arange(f1.shape[0]):
    for j in np.arange(f1.shape[1]):
        if (i+j)%2!=0:
            fil1[i,j]=-f1[i,j]

for i in np.arange(f2.shape[0]):
    for j in np.arange(f2.shape[1]):
        if (i+j)%2!=0:
            fil2[i,j]=-f2[i,j]


F1=np.fft.fft2(fil1)
mag1=20*np.log(np.abs(F1))
pha1=np.angle(F1)

F2=np.fft.fft2(fil2)
mag2=20*np.log(np.abs(F2))
pha2=np.angle(F2)

plt.figure(1)

plt.subplot(221)
plt.imshow(mag1, cmap='gray')
plt.axis('off')
plt.title("lenna256 magnitude")
plt.subplot(222)
plt.imshow(pha1, cmap='gray')
plt.axis('off')
plt.title("lenna256 phase")

plt.subplot(223)
plt.imshow(mag2, cmap='gray')
plt.axis('off')
plt.title("Synth magnitude")
plt.subplot(224)
plt.imshow(pha2, cmap='gray')
plt.axis('off')
plt.title("Synth phase")

plt.show()