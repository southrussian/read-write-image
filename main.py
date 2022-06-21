import cv2 as cv
from assets import assets
import sys


# def main():
#     file = assets.cat_image
#     image = cv.imread(file, cv.IMREAD_GRAYSCALE)
#
#     if image is None:
#         sys.exit('Could not read the image')
#
#     cv.imshow('Cat Image', image)
#     key = cv.waitKey(0)
#
#     if key == ord('s'):
#         cv.imwrite('outputCat.png', image)
#
#     cv.destroyAllWindows()
#     sys.exit('Finished!')

# if __name__ == '__main__':
#     main()

# video

# def play_video(file: str, webcam: bool = False):
#     if webcam:
#         video = cv.VideoCapture(0)
#     else:
#         video = cv.VideoCapture(file)
#
#     if not video.isOpened():
#         print('Error opening the video file')
#     else:
#         fps = video.get(cv.CAP_PROP_FPS)
#         frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
#         width, height = int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
#         frame_size = (width, height)
#
#         print('Video details:')
#         print('FPS:', round(fps, 2))
#         print('Frame count:', frame_count)
#         print(f'H {height}, W {width}')
#
#         codec = cv.VideoWriter_fourcc(*'mp4v')
#         output = cv.VideoWriter('output.mp4', codec, fps, frame_size)
#
#         while video.isOpened():
#             success, frame = video.read()
#
#             if success:
#                 cv.imshow('Frame', frame)
#                 output.write(frame)
#                 cv.waitKey(10)
#             else:
#                 print('Finished')
#                 break
#
#         video.release()
#         cv.destroyAllWindows
#
#
# if __name__ == '__main__':
#     play_video(file=assets.cat_video)

# resize the image

# def resize_image(percent: float):
#     file = assets.cat_image
#     image = cv.imread(file)
#
#     image_dimension = image.shape
#     print('Dimensions:', image_dimension)
#     height, width = image_dimension[:2]
#
#     new_height = int(height * percent)
#     new_width = int(width * percent)
#     new_dimension = (new_height, new_width)
#
#     resized = cv.resize(image, new_dimension, interpolation=cv.INTER_LINEAR)
#
#     print('New dimension:', resized.shape)
#     cv.imshow('Resized image', resized)
#     cv.waitKey(0)
#
#     cv.destroyAllWindows()
#     sys.exit('Finished')
#
#
# if __name__ == '__main__':
#     resize_image(0.1)

# crop the image

def crop_image():
    file = assets.cat_image
    image = cv.imread(file)

    print('Dimensions:', image.shape)
    print(image)

    cropped_image = image[150:450, 200:450]  # y - x
    cv.imshow('Cropped image', cropped_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    sys.exit('Finished')


if __name__ == '__main__':
    crop_image()