import numpy as np
import matplotlib.pyplot as plt
import pywt

# img=plt.imread('fingerprint.png')
img=plt.imread('boat.png')

# wavelet=pywt.Wavelet('db4')

coeffs=pywt.wavedec2(img, 'db4', mode=pywt.Modes.periodic, level=3)
rec_org=pywt.waverec2(coeffs, 'db4')


def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))
def normalize(d):
    d_new=d
    for i in range(len(d)):
        d_new[i]=(d[i]/np.abs(d[i]).max())

    return d_new
# def normalize(d):
#     return (d-np.min(d))/(np.max(d)-np.min(d))
# def normalize(d):
#     return d/np.abs(d).max()

coeffs[0]=normalize(coeffs[0])
for level in range(len(coeffs)-1):
    coeffs[level+1]=[normalize(d) for d in coeffs[level+1]]

arr, slices = pywt.coeffs_to_array(coeffs)

# for level in range(len(arr)):
#     for z in range(arr[0]):
#         mat=arr[level][z]
#         arr[level][z]=mat/np.max(mat)

plt.figure(1)
plt.imshow(arr, cmap='gray')

plt.figure(2)
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.imshow(rec_org, cmap='gray')
plt.subplot(133)
plt.imshow(rec_org-img, cmap='gray')

def MAE(x):
    return np.sum(np.abs(x))/np.size(x)

print(MAE(rec_org-img))


plt.show()