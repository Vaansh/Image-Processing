import cv2
import matplotlib.pyplot as plt


def programming_function_2(path="img/HawkesBay.jpeg", save_dir="img/programming"):
    image = cv2.imread(path, 0)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.title("Histogram of the image")
    plt.savefig(save_dir + "/Figure_2.jpeg")
    plt.show()
