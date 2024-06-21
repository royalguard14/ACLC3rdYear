import matplotlib.pyplot as plt

# Define the steps in the pipeline
pipeline_steps = [
    "Input Audio",
    "Preprocessing",
    "Feature Extraction (MFCCs)",
    "Wav2Vec2 Model",
    "GMM Training",
    "Classification",
    "Output"
]

# Define the connections between pipeline steps
connections = [
    (0, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 6),
    (4, 5),
    (5, 6)
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the pipeline steps
for i, step in enumerate(pipeline_steps):
    ax.text(0, i, step, ha='right', va='center', fontsize=12, fontweight='bold')

# Plot the connections between steps
for connection in connections:
    start_step = connection[0]
    end_step = connection[1]
    ax.plot([0, 1], [start_step, end_step], color='black')

# Hide axes
ax.axis('off')

# Add title
plt.title('Speech Processing Pipeline', fontsize=14, fontweight='bold')

# Show the plot
plt.tight_layout()
plt.show()
