import cv2
import numpy as np

image = cv2.imread('rgb.jpg', 0)
A = image.copy() / 255

m, n = A.shape

B = np.zeros((m, n));
i = 2
j = 2

for i in range(m - 1):
    for j in range(n - 1):
        B[i, j] = (A[i - 1, j - 1] + A[i - 1, j] + A[i - 1, j + 1]
                   + A[i, j - 1] + A[i, j] + A[i, j + 1]
                   + A[i + 1, j + 1] + A[i + 1, j] + A[i + 1, j + 1])
        B[i, j] = B[i, j] / 9;

cv2.imshow('Sin-filtro', image)
cv2.imshow('Con-filtro', B)

cv2.waitKey(0)
cv2.destroyAllWindows()

