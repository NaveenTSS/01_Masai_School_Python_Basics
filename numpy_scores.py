# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:27:35 2026

@author: tatas
"""

import numpy as np   # Import NumPy library for numerical operations

#==========================================
# Task 1: Generate and Inspect the Data
#==========================================

np.random.seed(42)   # Set random seed for reproducibility (same random numbers each run)

# Generate a 5x4 matrix of random integers between 50 and 100 (inclusive)
scores = np.random.randint(50, 101, (5, 4))

# Access specific elements and slices:
print(f"Score of the 3rd student in 2nd subject is {scores[2][1]}")  
# → Row index 2 (3rd student), Column index 1 (2nd subject)

print(f"All scores of the last 2 students \n{scores[-2:,:]}")  
# → Rows -2 onward (last 2 students), all columns

print(f"All scores for the first 3 students in subjects 2 and 3 only: \n{scores[:3,1:3]}")  
# → Rows 0–2 (first 3 students), Columns 1–2 (subjects 2 and 3)

#==========================================
# Task 2 — Analyze with Broadcasting
#==========================================

# Compute average score for each subject (column-wise mean)
average = np.mean(scores, axis=0)

print(f"Average score of each student is {np.round(average,2)}")  
# → Rounded to 2 decimal places

# Define a curve (bonus points) for each subject
curve = np.array([5, 3, 7, 2])

# Apply curve to all students’ scores using broadcasting
curved_scores = scores + curve

# Find the maximum score per student (row-wise max after curve)
row_max = np.max(curved_scores, axis=1)

print(f"Best subject score of each student after adding curve {row_max}")

#==========================================
# Task 3 — Normalize and Identify
#==========================================

# Reshape row_max to column vector (5x1) for broadcasting
row_max = row_max.reshape(5, 1)

# Find minimum score per student (row-wise min after curve)
row_min = np.min(curved_scores, axis=1)
row_min = row_min.reshape(5, 1)

# Compute range (max - min) for each student
range = row_max - row_min

# Normalize scores: (original score - min) / range
normalized_array = (scores - row_min) / range

# Find index of highest normalized score (student & subject position)
max_index = np.unravel_index(np.argmax(normalized_array), normalized_array.shape)

print(f"The highest marks recorded for a student is at row {max_index[0]} and column {max_index[1]}.")

# Identify all curved scores greater than 90
curved_scores[np.where(curved_scores > 90, True, False)]

