import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("funnel_data.csv")

print("Data:\n", df)

# Calculate conversion rate
df['Conversion %'] = df['Users'].pct_change() * 100

print("\nConversion Rates:\n", df)

# Plot funnel
plt.bar(df['Stage'], df['Users'])
plt.title("Marketing Funnel")
plt.xlabel("Stages")
plt.ylabel("Users")
plt.show()