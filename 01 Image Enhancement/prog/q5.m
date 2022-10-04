I = imread("img/HawkesBay.jpeg");
J = histeq(I)
imhist(J)
ylim([0, 7500])
saveas(gcf, "img/programming/Figure_5.png")