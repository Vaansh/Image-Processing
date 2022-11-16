from PIL import Image


def programming_function_1(
    path="img/HawkesBay.jpeg", save_dir="img/programming", fmt="JPEG"
):
    image = Image.open(path).convert("L")
    image.show()
    image.save(save_dir + "/Figure_1.jpeg", fmt)
