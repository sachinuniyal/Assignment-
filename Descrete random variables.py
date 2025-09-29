import numpy as np

# Distribution
values = [1, 2, 3]
probabilities = [0.25, 0.35, 0.40]

# Generate sample
sample = np.random.choice(values, size=1000, p=probabilities)

# Compute statistics
mean = np.mean(sample)
var = np.var(sample)
std = np.std(sample)

print("Empirical Mean:", mean)
print("Empirical Variance:", var)
print("Empirical Std Dev:", std)
