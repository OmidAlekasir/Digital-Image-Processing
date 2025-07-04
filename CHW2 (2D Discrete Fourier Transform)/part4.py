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
fm=np.fft.ifft2(np.abs(F1))
fm=np.abs(fm)
fm=(fm/np.max(fm))*255
# fm=20*np.log((fm/np.max(fm))*255)
plt.imshow(fm, cmap='gray')
plt.axis('off')
plt.title("Lenna Magnitude only")

plt.subplot(222)
fp=np.fft.ifft2(np.exp(1j*pha1))
fp=np.abs(fp)
fp=(fp/np.max(fp))*255
# fp=20*np.log(fp)
plt.imshow(fp, cmap='gray')
plt.axis('off')
plt.title("Lenna Phase only")

# plt.subplot(233)
# fp=np.fft.ifft2(F1)
# fp=np.abs(fp)
# plt.imshow(fp, cmap='gray')
# plt.axis('off')
# plt.title("Lenna iFFT")

plt.subplot(223)
fm=np.fft.ifft2(np.abs(F2))
fm=np.abs(fm)
fm=(fm/np.max(fm))*255
# fm=20*np.log((fm/np.max(fm))*255)
plt.imshow(fm, cmap='gray')
plt.axis('off')
plt.title("Synth Magnitude only")

plt.subplot(224)
fp=np.fft.ifft2(np.exp(1j*pha2))
fp=np.abs(fp)
fp=(fp/np.max(fp))*255
# fp=20*np.log(fp)
plt.imshow(fp, cmap='gray')
plt.axis('off')
plt.title("Synth Phase only")

# plt.subplot(236)
# fp=np.fft.ifft2(F2)
# fp=np.abs(fp)
# plt.imshow(fp, cmap='gray')
# plt.axis('off')
# plt.title("Circle iFFT")

plt.show()