clc
clear
close all

img=imread('lena_color.tif');
img_noisy=imnoise(img,'gaussian',0,0.25);

h=fspecial('motion',20,30);
img_motion=imfilter(img,h,'replicate','conv','circular');
img_motion_noisy=imfilter(img_noisy,h,'replicate');

img_res=deconvwnr(img_motion,h,0.00001);
img_noisy_inv=deconvwnr(img_motion_noisy,h,0);
img_noisy_res=deconvwnr(img_motion_noisy,h,0.05);
img_lse=deconvreg(img_motion_noisy,h);

% imshow(img_res)
% title('Motion-blur Restoration Result')


noise_inv=im2double(img-img_res);
noise_inv_n=im2double(img-img_noisy_inv);
noise_wnr=im2double(img-img_noisy_res);

RMS_signal=rms(rms(rms(img)));
RMS_noise_inv=rms(rms(rms(noise_inv)));
RMS_noise_inv_n=rms(rms(rms(noise_inv_n)));
RMS_noise_wnr=rms(rms(rms(noise_wnr)));

SNR_inv=(RMS_signal/RMS_noise_inv)^2;
SNR_inv_n=(RMS_signal/RMS_noise_inv_n)^2;
SNR_wnr=(RMS_signal/RMS_noise_wnr)^2;
SNRdb=10*log(SNR_inv)
SNRdb=10*log(SNR_inv_n)
SNRdb=10*log(SNR_wnr)

% subplot(1,2,1)
% imshow(img_noisy_res)
% title('Restoration - Wiener Filter')
% subplot(1,2,2)
imshow(img_lse)
title('Restoration - LSE')