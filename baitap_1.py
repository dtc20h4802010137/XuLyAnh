import os
import cv2

OUTPUT_FOLDER_PATH = "images/output/baitap_1"


def baitap_1():
    """
    1. Thực hiện đọc, ghi ảnh, lưu ảnh

    2. Chuyển từ ảnh màu sang ảnh đa mức xám

    3. Chuyển đổi các mô hình màu (HSV, LAB, RBG, BGR)
    """
    os.makedirs(OUTPUT_FOLDER_PATH, exist_ok=True)

    # 1. Đọc ảnh
    image = cv2.imread("images/test/test_image.jpg")
    cv2.waitKey(0)

    # 2. Ghi ảnh, lưu ảnh
    cv2.imwrite(f"{OUTPUT_FOLDER_PATH}/anh_da_luu.png", image)

    # 3. Chuyển sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("anh_xam", gray_image)
    cv2.waitKey(0)

    # 4. Chuyển đổi các mô hình màu khác
    # HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("anh_HSV", hsv_image)
    cv2.waitKey(0)

    # LAB
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    cv2.imshow("anh_LAB", lab_image)
    cv2.waitKey(0)

    # RGB (mặc định OpenCV đọc là BGR)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("anh_RGB", rgb_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


baitap_1()
