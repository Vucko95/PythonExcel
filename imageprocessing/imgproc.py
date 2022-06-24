import cv2


def imaginaro():
    image1 = cv2.imread('./imageprocessing/galaxy.jpeg', 0)
    image2 = cv2.imread('./imageprocessing/bear.jpeg', 0)
    image3 = cv2.imread('./imageprocessing/python.jpeg', 0)
    togray1 = cv2.imwrite('./grayimages/galaxy-gray.jpeg', image1)
    togray2 = cv2.imwrite('./grayimages/bear.jpeg', image2)
    togray3 = cv2.imwrite('./grayimages/python.jpeg', image3)


# print(color)
imaginaro()
