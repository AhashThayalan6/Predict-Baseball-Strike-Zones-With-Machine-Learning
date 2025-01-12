# Task 14: Optimize parameters
classifier = SVC(kernel='rbf', gamma=100, C=100)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
draw_boundary(ax, classifier)
accuracy = classifier.score(
    validation_set[['plate_x', 'plate_z']],
    validation_set['type']
)
print(f"Overfitted Accuracy: {accuracy}")

# Task 15: Experiment with hyperparameters
best_accuracy = 0
best_gamma, best_c = None, None
for gamma in [0.1, 1, 10, 100, 1000]:
    for c in [0.1, 1, 10, 100, 1000]:
        temp_classifier = SVC(kernel='rbf', gamma=gamma, C=c)
        temp_classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
        temp_accuracy = temp_classifier.score(
            validation_set[['plate_x', 'plate_z']],
            validation_set['type']
        )
        if temp_accuracy > best_accuracy:
            best_accuracy = temp_accuracy
            best_gamma, best_c = gamma, c

print(f"Best Accuracy: {best_accuracy} (Gamma: {best_gamma}, C: {best_c})")

# Task 16: Explore other players
def plot_player_data(player_data, ax_limits=(-3, 3, -2, 6)):
    data = player_data.dropna(subset=['plate_x', 'plate_z', 'type'])
    training_set, validation_set = train_test_split(data, random_state=1)
    
    classifier = SVC(kernel='rbf', gamma=best_gamma, C=best_c)
    classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

    fig, ax = plt.subplots()
    scatter = plt.scatter(
        x=data['plate_x'],
        y=data['plate_z'],
        c=data['type'],
        cmap=plt.cm.coolwarm,
        alpha=0.25
    )
    draw_boundary(ax, classifier)
    ax.set_xlim(ax_limits[:2])
    ax.set_ylim(ax_limits[2:])
    plt.colorbar(scatter)
    plt.xlabel('Plate X')
    plt.ylabel('Plate Z')
    plt.show()

plot_player_data(jose_altuve)
plot_player_data(david_ortiz)
