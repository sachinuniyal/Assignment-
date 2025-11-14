import matplotlib.pyplot as plt

# Generate 2000 samples from exponential with mean=5 (scale = mean)
samples = np.random.exponential(scale=5, size=2000)

# Plot histogram
plt.hist(samples, bins=30, density=True, alpha=0.6, color='skyblue', label="Histogram")

# Overlay theoretical PDF
x = np.linspace(0, max(samples), 200)
pdf = (1/5) * np.exp(-x/5)
plt.plot(x, pdf, 'r-', lw=2, label="PDF (λ=1/5)")

plt.title("Exponential Distribution (mean=5)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.show()
