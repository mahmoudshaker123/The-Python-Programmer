# Challenge 02 - Image Blurrer
# Write a program that takes an image and blurs the image.
# The image is represented as a list of lists, where each list represents a row of the image.
# Each element in the list is an integer representing a pixel value.
# The image should be blurred by taking the average of the pixel values of the surrounding pixels.
# The surrounding pixels are the pixels to the left, right, above, and below the current pixel.
# If there is no surrounding pixel, the pixel should remain the same.

# For example, the image:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# Should be blurred to:
# [
#     [2, 3, 4],
#     [3, 4, 5],
#     [5, 6, 7]
# ]


def blur_image(image: list[list[int]]) -> list[list[int]]: ...
