import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

img=plt.imread('lena_color.tif')
height=np.shape(img)[0]
width=np.shape(img)[1]
F=np.fft.fft2(img)

r=0.002
R=np.arange(r)
theta=0
T=1

theta=np.deg2rad(theta)
cs=np.cos(theta)
sn=np.sin(theta)
x=r*cs
y=r*sn

M=abs(int(r*cs))
N=abs(int(r*sn))

H=np.zeros((height,width),dtype=complex)

count=0
for u in np.arange(height):
    for v in np.arange(width):
        den=math.pi*(u*0.1+v*0)
        count+=1
        if den==0:
            H[u][v]=T
        else:
            H[u,v]=T*np.sinc(den)*np.exp(-1j*den)
        if np.abs(H[u,v])==0:
            H[u,v]=1

print(count)
print(np.shape(H))
h=np.fft.ifft2(H)
# print(np.shape(H))
G=np.zeros_like(F,dtype=complex)
G[:,:,0]=F[:,:,0]*H
G[:,:,1]=F[:,:,1]*H
G[:,:,2]=F[:,:,2]*H
# G=F*H
img_motion=np.abs(np.fft.ifft2(G))/255

plt.subplot(121)
plt.imshow(np.abs(h))
plt.title('Main Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_motion)
plt.title('Motion-blurred Image')
plt.axis('off')

plt.show()