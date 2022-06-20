import cv2 as cv
from assets import assets
import sys


def main():
    file = assets.cat_image
    image = cv.imread(file, cv.IMREAD_GRAYSCALE)

    if image is None:
        sys.exit('Could not read the image')

    cv.imshow('Cat Image', image)
    key = cv.waitKey(0)

    if key == ord('s'):
        cv.imwrite('outputCat.png', image)

    cv.destroyAllWindows()
    sys.exit('Finished!')


if __name__ == '__main__':
    main()
