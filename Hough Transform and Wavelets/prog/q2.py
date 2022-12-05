import cv2
import pywt
import pywt.data

import numpy as np
import matplotlib.pyplot as plt


def wavelet(wavelet, levels=3):
    image = cv2.imread("img/lena.tif")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.float32(image)

    _, ax = plt.subplots(1, 4, figsize=[7, 2.5])
    for level in range(levels + 1):
        if level == 0:
            ax[0].set_axis_off()
            ax[0].imshow(image, cmap=plt.cm.gray)
            ax[0].set_title("Original Image")
            ax[0].set_axis_off()
            cv2.imshow("Original Image", cv2.imread("img/lena.tif"))
            continue

        coeff = pywt.wavedec2(image, wavelet="db4", level=level)
        coeff[0] /= np.abs(coeff[0]).max()

        for l in range(level):
            coeff[l + 1] = [d / np.abs(d).max() for d in coeff[l + 1]]

        res, _ = pywt.coeffs_to_array(coeff)
        cv2.imshow("Level {}".format(level), res)
        ax[level].imshow(res, cmap=plt.cm.gray)
        ax[level].set_title("Level {}".format(level))
        ax[level].set_axis_off()

    plt.tight_layout()
    plt.savefig("img/prog/q2_{}.png".format(wavelet))
    plt.show()

    cv2.waitKey(0)


def main():
    wavelet("haar")
    wavelet("db4")


if __name__ == "__main__":
    main()
