# Generate 10,000 random numbers from uniform(0,1)
uniform_data = np.random.uniform(0, 1, 10000)

# Take 1000 samples of size 30, compute means
sample_means = []
for _ in range(1000):
    sample = np.random.choice(uniform_data, size=30)
    sample_means.append(np.mean(sample))

# Plot original uniform distribution
plt.hist(uniform_data, bins=30, density=True, alpha=0.6, color="green", label="Uniform Data")

plt.title("Uniform Distribution")
plt.show()

# Plot distribution of sample means
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color="orange", label="Sample Means")
plt.title("Distribution of Sample Means (CLT)")
plt.show()
