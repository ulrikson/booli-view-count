import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def generate_view_count_graph():
    # Read the CSV file
    df = pd.read_csv("property_data.csv")

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Sort by timestamp
    df = df.sort_values("timestamp")

    # Create the line plot
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["view_count"], marker="o")

    # Customize the plot
    plt.title("Property View Count Over Time")
    plt.xlabel("Time")
    plt.ylabel("View Count")
    plt.grid(True)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Show the plot interactively
    plt.show()


if __name__ == "__main__":
    generate_view_count_graph()
