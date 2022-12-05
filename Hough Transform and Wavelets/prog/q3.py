import cv2
import numpy as np


def main():
    image = cv2.imread("img/q3.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # invert, erode and invert back
    image = cv2.bitwise_not(image)
    eroded = cv2.erode(image, np.ones((9, 9), np.uint8), iterations=1)
    eroded = cv2.bitwise_not(eroded)
    cv2.imwrite("img/q3_output_1.png", eroded)

    # Gaussian blur to get rid of the small dots completely
    blurred = cv2.GaussianBlur(eroded, (5, 5), 0)
    blurred = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite("img/q3_output_2.png", blurred)

    # use Hough transform to get the number of circles
    res = blurred
    circles = cv2.HoughCircles(
        res,
        cv2.HOUGH_GRADIENT,
        1,
        res.shape[0] / 64,
        param2=17,
        minRadius=1,
        maxRadius=100,
    )
    res = cv2.cvtColor(res, cv2.COLOR_GRAY2BGR)

    assert circles is not None
    circles = np.uint16(np.around(circles))

    # construct circles around the dots
    for (a, b, c) in circles[0, :]:
        cv2.circle(res, (a, b), c, (0, 0, 255), 2)
        cv2.circle(res, (a, b), 2, (255, 255, 0), 3)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        res,
        "Number of Dots Counted: {}".format(circles.shape[1]),
        (1, 400),
        font,
        1,
        (0, 0, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.imwrite("img/q3_output_3.png", res)


if __name__ == "__main__":
    main()
