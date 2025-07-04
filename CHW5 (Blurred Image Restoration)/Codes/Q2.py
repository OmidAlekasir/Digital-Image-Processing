import numpy as np
import matplotlib.pyplot as plt
import cv2

img=plt.imread('lena_color.tif')
height=np.shape(img)[0]
width=np.shape(img)[1]

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

noise=np.random.normal(0,0.25**0.5,(height,width,3))*150

img_noisy=img+noise
img_motion_noisy=img_motion+noise

img_noisy/=255
img_motion_noisy/=255


plt.subplot(121)
plt.imshow(img_noisy)
plt.title('Main Image - Noisy')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_motion_noisy)
plt.title('Motion-blurred Image - Noisy')
plt.axis('off')

plt.show()

print(np.max(img))
print(np.max(noise))