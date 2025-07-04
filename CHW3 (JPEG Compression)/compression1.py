import numpy as np
import matplotlib.pyplot as plt
import cv2

def selectQMatrix(qName):
    Q10=np.array([[80, 60, 50, 80, 120, 200, 255, 255],
                [55,60,70,95,130,255,255,255],
                [70,65,80,120,200,255,255,255],
                [70,85,100,145,255,255,255,255],
                [90,110,185,255,255,255,255,255],
                [120,175,255,255,255,255,255,255],
                [245,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255]])

    Q50=np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                [12,12,14,19,26,58,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,29,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,130,99]])

    Q90=np.array([[3, 2, 2, 3, 5, 8, 10, 12],
                [2,2,3,4,5,12,12,11],
                [3,3,3,5,8,11,14,11],
                [3,3,4,6,10,17,16,12],
                [4,4,7,11,14,22,21,15],
                [5,7,11,13,16,12,23,18],
                [10,13,16,17,21,24,24,21],
                [14,18,19,20,22,20,20,20]])

    if qName=="Q10":
        return Q10
    elif qName=="Q50":
        return Q50
    elif qName=="Q90":
        return Q90
    else:
        return np.ones((8,8))


##########
img=plt.imread('barbara_gray.bmp')
img=img-128


wid=len(img[1,:])
hei=len(img[:,1])
block=8

sliced=np.zeros([8,8,int(wid/block),int(hei/block)])
dct=np.zeros_like(sliced)
invlist=np.zeros_like(sliced)
img_new=np.zeros_like(img)
Qmat=selectQMatrix("Q10")


for i in np.arange(int(wid/block)):
    for j in np.arange(int(hei/block)):
        sliced[:,:,i,j]=img[i*block:(i+1)*block,j*block:(j+1)*block]


for i in np.arange(int(wid/block)):
    for j in np.arange(int(hei/block)):
        dct[:,:,i,j]=np.round(cv2.dct(sliced[:,:,i,j])/Qmat)


for i in np.arange(int(wid/block)):
    for j in np.arange(int(hei/block)):
        invlist[:,:,i,j]=cv2.idct(dct[:,:,i,j]*Qmat)

for i in np.arange(int(wid/block)):
    for j in np.arange(int(hei/block)):
        img_new[i*block:(i+1)*block,j*block:(j+1)*block]=invlist[:,:,i,j]


# img_new=(img_new)/(np.max(img_new))
# img_new=(img_new)/(np.max(img_new))
# print(img_new)
# img_new*=255
# img=img+128
# print(np.min(img_new))

img+=128
img_new+=128

plt.figure(1)

# plt.subplot(121)
# plt.imshow(img, cmap='gray')
# plt.subplot(122)
plt.imshow(img_new, cmap='gray')

plt.show()