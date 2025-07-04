import numpy as np
import matplotlib.pyplot as plt
import cv2

img=plt.imread('lena_color.tif')

r=20
theta=90+45
theta=np.deg2rad(theta)
cs=np.cos(theta)
sn=np.sin(theta)

M=abs(int(r*cs))
N=abs(int(r*sn))

motion_ker=np.zeros((M,N))
for i in np.arange(r):
    x=int(i*cs)
    y=int(i*sn)
    if cs<0:
        x+=M-1
    if sn<0:
        y+=N-1

    motion_ker[x,y]=1

motion_ker/=np.sum(motion_ker)
img_motion = cv2.filter2D(img,-1,motion_ker)

# F=np.fft.fft2(img)
# G=np.fft.fft2(img_motion)

H=np.fft.fft2(motion_ker)
# motion_res_ker=abs(np.fft.ifft2(1/H))
# print(motion_res_ker)
# img_res = cv2.filter2D(img_motion/255,-1,motion_res_ker)/255


plt.subplot(121)
plt.imshow(img)
plt.title('Main Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_motion)
plt.title('Motion-blurred Image')
plt.axis('off')

plt.show()