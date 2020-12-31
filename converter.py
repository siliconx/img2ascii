#!/usr/bin/env python3
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

# dimension of ascii image
DIMENSION = (64, 64)

# character pixles (grayscale: darker -> brighter)
# two charcters per pixle
# you can add any other characters if you like
CHAR_PIXLES = ['@@', '$$', '&&', '**', '\\\\', ';;', '::', '..', '  ']

# read image as grayscale image
img = cv2.imread(sys.argv[1], 0)

# resize to given dimension
img = cv2.resize(img, DIMENSION)

# uncomment to show the scaled image
# plt.imshow(img, cmap='gray')
# plt.show()

# min and max graylevel
max_ = np.max(img)
min_ = np.min(img)


def to_ascii(x):
    """Convert a integer pixle to ASCII character."""
    idx = int(
        ((x - min_) / (max_-min_+1)) * len(CHAR_PIXLES))
    return CHAR_PIXLES[idx]


# function vectorization by numpy
to_ascii_vec = np.vectorize(to_ascii)
char_img = to_ascii_vec(img)

# output
for row in char_img:
    for e in row:
        print(e, end='')
    print()
