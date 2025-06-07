import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion, binary_dilation


def trim_zeros_border(arr):
    rows = np.any(arr, axis=1)
    cols = np.any(arr, axis=0)
    return arr[np.ix_(rows, cols)]


# I = np.array(
#     [
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 1, 1, 1, 1, 0],
#         [0, 0, 1, 0, 1, 0, 0],
#         [0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#     ],
#     dtype=bool,
# )

# T = np.array([[1, 0], [1, 1]], dtype=bool)

# I = np.array(
#     [
#         [0, 1, 0, 0],
#         [1, 1, 1, 0],
#         [0, 0, 1, 1],
#         [0, 1, 1, 0],
#         [0, 1, 1, 1],
#     ],
#     dtype=bool,
# )

# structure = np.array([[1], [1]], dtype=bool)

I = np.array(
    [
        [0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
    ],
    dtype=bool,
)

structure = np.array([[1], [1]], dtype=bool)

I_padded = np.pad(I, pad_width=1, mode="constant", constant_values=0)

Erosion = binary_erosion(I, structure)

Dilation = binary_dilation(I_padded, structure)
Dilation_trimmed = trim_zeros_border(Dilation)

Opening = binary_dilation(Erosion, structure)
Closing = binary_erosion(Dilation_trimmed, structure)
Closing_trimmed = trim_zeros_border(Closing)


print("Default (I):")
print(I.astype(int))

print("\nErosion (E(I)):")
print(Erosion.astype(int))

print("\nDilation (D(I)):")
print(Dilation.astype(int))
print("\nDilation trimmed (D(I)):")
print(Dilation_trimmed.astype(int))

print("\nOpening (E(D(I))):")
print(Opening.astype(int))

print("\nClosing (D(E(I))):")
print(Closing.astype(int))
print("\nClosing trimmed (D(E(I))):")
print(Closing_trimmed.astype(int))
