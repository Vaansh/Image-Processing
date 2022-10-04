import matplotlib.pyplot as plt
import numpy as np

from prog.q1 import programming_function_1
from prog.q2 import programming_function_2
from prog.q4 import programming_function_4


def theory_function_3a():
    x = np.arange(16)
    y = np.array([0, 5, 13, 57, 100, 39, 21, 12, 7, 2, 0, 0, 0, 0, 0, 0])

    plt.bar(x, y, color="orange")

    plt.xlabel("Gray level (GP)")
    plt.ylabel("Number of pixels (NP)")

    plt.gca().set_xlim([0, 16])

    plt.title("Histogram of given image")
    plt.xticks(np.arange(0, 16, 1.0))

    plt.savefig("img/theory/Figure_3a.png", dpi=95)
    plt.show()


def theory_function_3bii():
    p_rk_x = np.arange(16)
    p_rk_y = np.array([
        0, 0.01953125, 0.05078125, 0.22265625, 0.390625, 0.15234375,
        0.08203125, 0.046875, 0.02734375, 0.0078125, 0, 0, 0, 0, 0, 0
    ])

    p_sk_x = np.array([0, 1, 4, 10, 13, 14, 15])
    p_sk_y = np.array([
        0.01953125, 0.05078125, 0.22265625, 0.390625, 0.15234375, 0.12890625,
        0.03515625
    ])

    plt.bar(p_rk_x, p_rk_y, color="deepskyblue")
    plt.xlabel("$r_k$")
    plt.ylabel("$p_r(r_k)$")
    plt.title("Original histogram")
    plt.xticks(np.arange(0, 16, 1.0))
    plt.tight_layout()
    plt.savefig("img/theory/Figure_3bii1.png", dpi=95)
    plt.show()

    plt.bar(p_sk_x, p_sk_y, color="red")
    plt.xlabel("$s_k$")
    plt.ylabel("$p_s(s_k)$")
    plt.xticks(np.arange(0, 16, 1.0))
    plt.tight_layout()
    plt.title("Equalized histogram")
    plt.savefig("img/theory/Figure_3bii2.png", dpi=95)
    plt.show()


def theory_function_3c():
    s_k_x = np.array([0, 1, 4, 10, 13, 14, 15])
    n_k_y = np.array([5, 13, 57, 100, 39, 33, 9])

    plt.bar(s_k_x, n_k_y, color="magenta")

    plt.xlabel("$s_k$")
    plt.ylabel("$n_k$")

    plt.gca().set_xlim([0, 16])

    plt.title("Resulting histogram")
    plt.xticks(np.arange(0, 16, 1.0))

    plt.savefig("img/theory/Figure_3c.png", dpi=95)
    plt.show()


if __name__ == "__main__":
    # Theory part
    theory_function_3a()
    theory_function_3bii()
    theory_function_3c()

    # Programming part
    programming_function_1()
    programming_function_2()
    programming_function_4()
