# Task 9: Split the data
training_set, validation_set = train_test_split(data, random_state=1)

# Task 10: Create an SVM
classifier = SVC(kernel='rbf')

# Task 11: Train the SVM
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

# Task 12: Visualize the decision boundary
draw_boundary(ax, classifier)

# Task 13: Calculate accuracy
accuracy = classifier.score(
    validation_set[['plate_x', 'plate_z']],
    validation_set['type']
)
print(f"Initial Accuracy: {accuracy}")
