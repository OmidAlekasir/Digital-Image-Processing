import numpy as np
import matplotlib.pyplot as plt
import pywt

img=plt.imread('boat.png')

# wt1=pywt.dwt2(img, 'haar')[1]

wavelet=pywt.Wavelet('db4')

plt.subplot(221)
plt.plot(wavelet.dec_lo, '--*')
plt.title('Decomposition - Low')
plt.subplot(222)
plt.plot(wavelet.dec_hi, '--*')
plt.title('Decomposition - High')
plt.subplot(223)
plt.plot(wavelet.rec_lo, '--*')
plt.title('Reconstruction - Low')
plt.subplot(224)
plt.plot(wavelet.rec_hi, '--*')
plt.title('Reconstruction - High')


plt.show()