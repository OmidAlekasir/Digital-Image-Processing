import numpy as np
import matplotlib.pyplot as plt
import pywt

# img=plt.imread('flinstones.png')[:,:,0]
img=plt.imread('boat.png')
# img=plt.imread('peppers256.png')

coeffs_3=pywt.wavedec2(img, 'db4', mode=pywt.Modes.periodic, level=3)
coeffs_4=pywt.wavedec2(img, 'db4', mode=pywt.Modes.periodic, level=4)
coeffs_5=pywt.wavedec2(img, 'db4', mode=pywt.Modes.periodic, level=5)
coeffs_6=pywt.wavedec2(img, 'db4', mode=pywt.Modes.periodic, level=6)

approx_3=coeffs_3[0]
approx_4=coeffs_4[0]
approx_5=coeffs_5[0]
approx_6=coeffs_6[0]

plt.figure(1)
# plt.subplot(221)
# plt.imshow(img, cmap='gray')
# plt.title('Original')
# plt.axis('off')
plt.subplot(141)
plt.imshow(approx_3, interpolation='bilinear', cmap='gray')
plt.title('Approx, DL=3')
plt.axis('off')
plt.subplot(142)
plt.imshow(approx_4, interpolation='bilinear', cmap='gray')
plt.title('Approx, DL=4')
plt.axis('off')
plt.subplot(143)
plt.imshow(approx_5, interpolation='bilinear', cmap='gray')
plt.title('Approx, DL=5')
plt.axis('off')
plt.subplot(144)
plt.imshow(approx_6, interpolation='bilinear', cmap='gray')
plt.title('Approx, DL=6')
plt.axis('off')

plt.show()