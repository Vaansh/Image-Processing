I = imread("img/HawkesBay.jpeg");
imhist(I)
ylim([0, 7000])
saveas(gcf, "img/programming/Figure_3.png")