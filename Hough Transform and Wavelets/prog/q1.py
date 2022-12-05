import cv2
from PIL import Image
import numpy as np


def otsu(image, filename="q1_a"):
    (
        value,
        threshold,
        variance,
        max_variance,
        pixel_difference,
        sum_difference,
        cumulative_sum,
        cumulative_mean,
        global_intensity_mean,
    ) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

    # 1. Compute the normalized histogram of the input image
    histogram, num_pixels = (
        np.histogram(
            [
                image.getpixel((width, height))
                for height in range(image.size[1])
                for width in range(image.size[0])
            ],
            range(257),
        ),
        image.size[0] * image.size[1],
    )

    # 2. Compute the cumulative sums
    total_sum = sum(i * histogram[0][i] for i in range(256))

    for i in range(256):
        value += histogram[0][i]
        if num_pixels <= value:
            break

        pixel_difference = num_pixels - value

        # 3. Compute the cumulative means
        cumulative_sum += i * histogram[0][i]
        sum_difference = total_sum - cumulative_sum

        # 4. Compute the global intensity mean
        global_intensity_mean, cumulative_mean = (
            cumulative_sum / value,
            sum_difference / pixel_difference,
        )

        # 5. Compute the between - class variance
        variance = (
            value * pixel_difference * (global_intensity_mean - cumulative_mean) ** 2
        )

        # 6. Obtain the Otsu's threshold
        if variance > max_variance:
            max_variance = variance
            threshold = i

    res = [
        0 if (image.getpixel((height, width)) <= threshold) else 255
        for width in range(0, image.size[1])
        for height in range(0, image.size[0])
    ]
    image.putdata(res)
    image.save("img/prog/{}.png".format(filename))


def q1_a():
    image = Image.open("img/tools_noisy.png")
    otsu(image.convert("L"))


def q1_b():
    # blur image first
    image = cv2.imread("img/tools_noisy.png")
    image = cv2.blur(image, (5, 5))
    image = Image.fromarray(image)
    image.save("img/prog/q1_b_1.png")
    otsu(image.convert("L"), filename="q1_b_2")


def main():
    q1_a()
    q1_b()


if __name__ == "__main__":
    main()
