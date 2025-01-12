# Task 17: Add additional features
# Example: Adding 'strikes' as an additional feature
data = aaron_judge.dropna(subset=['plate_x', 'plate_z', 'type', 'strikes'])
training_set, validation_set = train_test_split(data, random_state=1)

classifier = SVC(kernel='rbf', gamma=best_gamma, C=best_c)
classifier.fit(training_set[['plate_x', 'plate_z', 'strikes']], training_set['type'])

accuracy = classifier.score(
    validation_set[['plate_x', 'plate_z', 'strikes']],
    validation_set['type']
)
print(f"Accuracy with additional feature 'strikes': {accuracy}")
