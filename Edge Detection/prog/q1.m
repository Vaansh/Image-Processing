% Load and process images
H = imread("house.tif");
H = H(:, :, 1);
H = im2double(H);

J = imread("jet.tif");
J = J(:, :, 1);
J = im2double(J);

% Separate images into magnitude 
% & phase angle using 2D fft
Hfft = fft2(H);
Fa = abs(Hfft);
Oa = angle(Hfft);

Jfft = fft2(J);
Fb = abs(Jfft);
Ob = angle(Jfft);

% Construct images as required
Ifd1 = Fa .* exp(j * Ob);
I1 = ifft2(Ifd1);

Ifd2 = Fb .* exp(j * Oa);
I2 = ifft2(Ifd2);

Ifd3 = Fa .* exp(j * Oa);
I3 = ifft2(Ifd3);

Ifd4 = Fb .* exp(j * Ob);
I4 = ifft2(Ifd4);

% Output images
montage({I1, I2, I3, I4});
title({"Top: I1 (Fa & Ob) vs I2 (Fb & Oa)",
    "Bottom: I3 (Fa & Oa) vs I4 (Fb & Ob)"})
