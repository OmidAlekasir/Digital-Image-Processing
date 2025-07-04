import numpy as np
import matplotlib.pyplot as plt
import pywt

# img=plt.imread('flinstones.png')[:,:,0]
# img=plt.imread('boat.png')
# img=plt.imread('peppers256.png')
img=plt.imread('lena.png')
# img=plt.imread('house.png')

def MSE(img):
    return np.sqrt(np.sum(img*img))/(np.shape(img)[0]*np.shape(img)[1])
def ABS(img):
    return np.sqrt(np.sum(img*img))

mean=0
sigma=100
noise = np.random.normal(mean, sigma, (np.shape(img)[0], np.shape(img)[1]))
img_noisy = img + (1/(10*sigma))*noise

mse=MSE(img-img_noisy)
PSNR=20*np.log(np.max(img)/np.sqrt(mse))

########################################################
coeffs=pywt.wavedec2(img_noisy, 'db4', mode=pywt.Modes.periodic, level=2)
arr1, slices=pywt.coeffs_to_array(coeffs)

# n=np.shape(detail)[0]*np.shape(detail)[1]

def denoise(arr,x1,x2,y1,y2):
    detail=arr[x1:x2][y1:y2]
    T=sigma*np.sqrt(2*np.log(np.size(detail)))
    abs_val=ABS(detail)
    if abs_val<T:
        return np.zeros_like(detail)
    else:
        return detail

# bounds=[len(coeffs[level+1][0]) for level in range(len(coeffs)-1)]
# print(bounds)

# arr1[0:69][0:69]=denoise(arr1, 0,69,0,69)
# arr1[70:139][0:69]=denoise(arr1, 70,139,0,69)
# arr1[0:69][70:139]=denoise(arr1, 0,69,70,139)
# arr1[70:139][70:139]=denoise(arr1, 70,139,70,139)

arr1[0:139][140:272]=denoise(arr1, 0,139,140,272)
arr1[140:272][0:139]=denoise(arr1, 140,272,0,139)
arr1[140:272][140:272]=denoise(arr1, 140,272,140,272)

arr1[0:531][273:531]=denoise(arr1, 0,531,273,531)
arr1[273:531][0:531]=denoise(arr1, 273,531,0,531)
arr1[273:531][273:531]=denoise(arr1, 273,531,273,531)

new_coeffs=pywt.array_to_coeffs(arr1, slices, output_format='wavedec2')
denoised=pywt.waverec2(new_coeffs, 'db4')


# T=sigma*np.sqrt(2*np.log(img.size))

# a=np.zeros_like(coeffs[1][0])

# coeffs_new=coeffs
# coeffs_new[1]=list(coeffs)
# print(type(coeffs_new[1]))
# print(type(coeffs[1]))
# for level in range(len(coeffs)-1):
#     coeffs_new[level+1]=list(coeffs[level+1])
#     for d in range(len(coeffs[level+1])):
#         detail=coeffs_new[level+1][d]
#         n=np.shape(detail)[0]*np.shape(detail)[1]
#         T=sigma*np.sqrt(2*np.log(n))
#         abs_val=ABS(detail)
#         if abs_val<T:
#             coeffs_new[level+1][d]=np.zeros_like(coeffs[level+1][d])
#         else:
#             coeffs_new[level+1][d]=coeffs[level+1][d]
#     # coeffs[level+1]=new_coeff

# arr2, slices=pywt.coeffs_to_array(coeffs)

plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(132)
plt.imshow(img_noisy, cmap='gray')
plt.title(r'Noisy Image - $\sigma$=100')
plt.axis('off')
plt.subplot(133)
plt.imshow(denoised, cmap='gray')
plt.title('Denoised Image - DL=2')
plt.axis('off')

mse=MSE(img-img_noisy)
PSNR=20*np.log(np.max(img)/np.sqrt(mse))
print(PSNR)
mse=MSE(img-denoised)
PSNR=20*np.log(np.max(img)/np.sqrt(mse))
print(PSNR)

plt.show()