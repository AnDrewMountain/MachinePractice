import pandas as pd
import numpy as np

np.random.seed(42)

#Generate synthetic data
num_samples = 200
feature_1 = np.random.rand(num_samples) * 100  # Random values between 0 and 100
feature_2 = np.random.rand(num_samples) * 50   # Random values between 0 and 50
feature_3 = np.random.randint(0, 2, num_samples)  # Random 0 or 1

# Create a DataFrame
df = pd.DataFrame({
    'Feature1': feature_1,
    'Feature2': feature_2,
    'Feature3': feature_3
})

# Save the DataFrame to a CSV file
output_path = 'data/synthetic_dataset.csv'  # Adjust path to be relative
df.to_csv(output_path, index=False)


print(f"Dataset created and saved to {output_path}")