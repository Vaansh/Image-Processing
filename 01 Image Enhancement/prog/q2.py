from PIL import Image
import matplotlib.pyplot as plt


def programming_function_2(path="img/HawkesBay.jpeg", save_dir="img/programming"):
    # creates 256 "buckets"
    grey_levels = list(range(256))

    # gets dimensions and loops over every pixel and
    # adds 1 otherwise 0 to each "bucket"
    image = Image.open(path)
    wid, hgt = image.size
    num_pixels = [
        sum(
            [
                1 if (image.getpixel((w, h)) == l) else 0
                for h in range(hgt)
                for w in range(wid)
            ]
        )
        for l in grey_levels
    ]

    plt.bar(grey_levels, num_pixels)
    plt.xlabel("Gray Level")
    plt.ylabel("Number of pixels")
    plt.title("Histogram of the image")
    plt.savefig(save_dir + "/Figure_2.jpeg")
    plt.show()
