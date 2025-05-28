import cv2


def show_image_scaled(window_name, image, scale=0.5):
    height, width = image.shape[:2]
    resized = cv2.resize(image, (int(width * scale), int(height * scale)))
    cv2.imshow(window_name, resized)
