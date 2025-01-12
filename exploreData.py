import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

# Task 1: Explore the data
print(aaron_judge.columns)  # Print column names

# Task 2: Understand pitch descriptions
print(aaron_judge['description'].unique())  # Unique values in 'description'

# Task 3: Explore the 'type' column
print(aaron_judge['type'].unique())  # Unique values in 'type'
