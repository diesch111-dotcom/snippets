#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" np_statistics.py

NumPy is the backbone of data science in Python, and its statistical 
module is incredibly powerful. It allows you to perform fast, vectorized 
operations on data arrays without writing slow for loops.

np.mean(a): Calculates the arithmetic mean (average).
np.median(a): Finds the middle value of the data.
np.std(a): Computes the standard deviation (measure of data spread).
np.var(a): Computes the variance (square of the standard deviation).

np.min(a) / np.max(a): Returns the minimum or maximum value.
np.ptp(a): "Peak-to-peak" — returns the range of the data 
    ($\text{maximum} - \text{minimum}$).
np.percentile(a, q): Computes the q-th percentile 
    (e.g., 90th percentile).
np.quantile(a, q): Similar to percentile, but 'q' is between 0 and 1.

np.corrcoef(x, y): Returns the Pearson product-moment correlation coefficient 
    matrix.
np.cov(x, y): Computes the covariance matrix.
np.histogram(a, bins=10): Computes the histogram of a dataset 
    (returns counts and bin edges).   

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
"""

import numpy as np

data = np.array([10, 20, 12, 15, 28, 14])

print("data =", data)
print("Mean:", np.mean(data))      # Output: 16.5
print("Median:", np.median(data))  # Output: 14.5
print("Std Dev:", np.std(data))    # Output: 5.937

print("Range (PTP):", np.ptp(data))        # 18    (28 - 10)
print("75th Percentile:", np.percentile(data, 75))  # 18.75


print("axis=1 collapses the columns (calculates row-wise).")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Column-wise mean (collapsing rows)
print(np.mean(matrix, axis=0))  # [2.5, 3.5, 4.5]

# Row-wise mean (collapsing columns)
print(np.mean(matrix, axis=1))  #  [2. , 5. ]

print("look at relationships between multiple variables.")

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

print("x =", x)
print("y =", y)
# Correlation matrix
print("np.corrcoef(x, y) =\n",np.corrcoef(x, y))


# NumPy provides "NaN-safe" alternatives that ignore missing values entirely
dirty_data = np.array([1, 2, np.nan, 4, 5])

print(np.mean(dirty_data))     # Output: nan
print(np.nanmean(dirty_data))  # Output: 3.0

