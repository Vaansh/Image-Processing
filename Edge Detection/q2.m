I = imread("img/house.tif");
I = I(:, :, 1);

L = edge(I, "LoG");
C = edge(I, "Canny");

montage({L, C})
title("Laplacian of Gaussian Vs. Canny edge detectors")
