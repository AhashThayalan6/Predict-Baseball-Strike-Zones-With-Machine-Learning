# Task 4: Map 'type' column to binary values
aaron_judge['type'] = aaron_judge['type'].map({'S': 1, 'B': 0})
print(aaron_judge['type'])  # Confirm transformation

# Task 6: Look at 'plate_x' and 'plate_z'
print(aaron_judge['plate_x'].head())  # Preview 'plate_x'
print(aaron_judge['plate_z'].head())  # Preview 'plate_z'

# Task 7: Drop rows with NaN values
data = aaron_judge.dropna(subset=['plate_x', 'plate_z', 'type'])

# Task 8: Plot the pitches
fig, ax = plt.subplots()
scatter = plt.scatter(
    x=data['plate_x'],
    y=data['plate_z'],
    c=data['type'],
    cmap=plt.cm.coolwarm,
    alpha=0.25
)

plt.colorbar(scatter)
plt.xlabel('Plate X')
plt.ylabel('Plate Z')
