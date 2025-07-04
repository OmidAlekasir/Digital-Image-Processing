import numpy as np
import matplotlib.pyplot as plt
import cv2

img=plt.imread('lena_color.tif')

r=20
theta=90+30
theta=np.deg2rad(theta)

M=abs(int(r*np.cos(theta)))
N=abs(int(r*np.sin(theta)))

motion_ker=np.zeros((M,N))
for i in np.arange(r):
    x=int(i*np.cos(theta))
    y=int(i*np.sin(theta))
    if x<0:
        x+=M-1
    if y<0:
        y+=N-1

    motion_ker[x,y]=1

# motion_ker=np.eye(10,18)
motion_ker/=np.sum(motion_ker)
img_motion = cv2.filter2D(img,-1,motion_ker)


plt.subplot(121)
plt.imshow(img)
plt.title('Main Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_motion)
plt.title('Motion-blurred Image')
plt.axis('off')

plt.show()