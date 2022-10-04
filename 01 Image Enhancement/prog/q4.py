from itertools import accumulate
from PIL import Image
import matplotlib.pyplot as plt


def programming_function_4(path="img/HawkesBay.jpeg", save_dir="img/programming"):
    image = Image.open(path)
    grey_levels = list(range(256))
    wid, hgt = image.size

    n_k = [
        sum(
            [
                1 if (image.getpixel((w, h)) == p) else 0
                for h in range(hgt)
                for w in range(wid)
            ]
        )
        for p in grey_levels
    ]

    L = wid * hgt
    pr_rk = [n / L for n in n_k]
    sk = [round(s * 255) for s in accumulate(pr_rk)]

    res_nk = [
        sum([n_k[i] if l == sk_r else 0 for i, sk_r in enumerate(sk)]) \
            for l in grey_levels
    ]

    plt.bar(grey_levels, res_nk)
    plt.xlabel("Gray Level")
    plt.ylabel("Number of pixels")
    plt.title("Histogram of the image")
    plt.savefig(save_dir + "/Figure_4.jpeg")
    plt.show()
