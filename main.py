import pandas as pd
import matplotlib.pyplot as plt

# Load the telemetry data
df = pd.read_csv("telemetry.csv")
df.columns = [col.strip() for col in df.columns]

# Display the first few rows
print(df.head())

# Show the exact column names
print("\nColumn names detected:")
print(df.columns)

plt.figure(figsize=(12, 6))

plt.plot(df["Time"], df["Speed"], label="Speed (kph)")

plt.plot(df["Time"], df["Throttle"], label="Throttle (%)")

plt.plot(df["Time"], df["Brake"], label="Brake (%)")

plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Telemetry Data Over Time")
plt.grid(True)
plt.tight_layout()

plt.show()

# Calculate max speed and average throttle
max_speed = df["Speed"].max()
avg_throttle = df["Throttle"].mean()

print(f"\nMax Speed: {max_speed:.2f} kph")
print(f"Average Throttle: {avg_throttle:.2f}%")

summary = {
    "Max Speed (kph)": [max_speed],
    "Average Throttle (%)": [avg_throttle]
}

summary_df = pd.DataFrame(summary)

summary_df.to_csv("summary.csv", index=False)

print("\nSummary saved to summary.csv")