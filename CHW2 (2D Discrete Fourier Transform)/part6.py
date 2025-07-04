import numpy as np
import matplotlib.pyplot as plt

f1=plt.imread("lenna256.gif")[:,:,0]
f2=plt.imread("Synth.tif")

F1=np.fft.fft2(f1)
M=f1.shape[0]
N=f1.shape[1]
x0=M/2
y0=N/2
for i in np.arange(M):
    for j in np.arange(N):
        F1[i,j]=F1[i,j]*np.exp(-2j*np.pi*((i*x0)/M+(j*y0)/N))

F2=np.fft.fft2(f2)
M=f2.shape[0]
N=f2.shape[1]
x0=M/2
y0=N/2
for i in np.arange(M):
    for j in np.arange(N):
        F2[i,j]=F2[i,j]*np.exp(-2j*np.pi*((i*x0)/M+(j*y0)/N))

plt.figure(1)

plt.subplot(121)
f1=np.fft.ifft2(F1)
f1=np.abs(f1)
plt.imshow(f1, cmap='gray')
plt.axis('off')
plt.title("Lenna Translation")

plt.subplot(122)
f2=np.fft.ifft2(F2)
f2=np.abs(f2)
plt.imshow(f2, cmap='gray')
plt.axis('off')
plt.title("Circle Translation")

plt.show()