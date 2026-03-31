import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display first few rows (optional)
print("Data Preview:\n", df.head())

# Assuming column name is 'Marks' (change if needed)
data = df['Marks']

# Calculations
mean_value = data.mean()
median_value = data.median()
mode_value = data.mode()
min_value = data.min()
max_value = data.max()
variance_value = data.var()
std_dev_value = data.std()

# Output
print("\n--- Central Tendencies ---")
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value.tolist())

print("\n--- Dispersion Measures ---")
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)
