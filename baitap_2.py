import cv2
from utils import show_image_scaled


def read_images(img_path1, img_path2):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    if img1 is None or img2 is None:
        raise ValueError("Không thể đọc một trong hai ảnh. Kiểm tra lại đường dẫn.")

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    return img1, img2


def add_images(img1, img2, alpha=None, output_path=None):
    if alpha is None:
        result = cv2.add(img1, img2)
    else:
        result = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

    if output_path:
        cv2.imwrite(output_path, result)

    return result


def subtract_images(img1, img2, output_path=None):
    result = cv2.subtract(img1, img2)

    if output_path:
        cv2.imwrite(output_path, result)

    return result


IMAGE_PATH_1 = "images/test/test_image_2.jpg"
IMAGE_PATH_2 = "images/test/test_image_3.jpg"

img1, img2 = read_images(IMAGE_PATH_1, IMAGE_PATH_2)

img_added = add_images(img1, img2)
show_image_scaled("Cong hai anh", img_added)
cv2.waitKey(0)

img_blended = add_images(img1, img2, 0.6)
show_image_scaled("Cong hai anh voi trong so", img_blended)
cv2.waitKey(0)

img_subtracted = subtract_images(img1, img2)
show_image_scaled("Tru hai anh", img_subtracted)
cv2.waitKey(0)
