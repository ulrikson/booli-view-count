import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


def generate_view_count_graph():
    # Set Seaborn style
    sns.set_theme(style="darkgrid")
    sns.set_palette("husl")

    # Read the CSV file
    df = pd.read_csv("property_data.csv")

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Sort by timestamp
    df = df.sort_values("timestamp")

    # Create the line plot with Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="timestamp", y="view_count", marker="o", linewidth=2)

    # Customize the plot
    plt.title("Property View Count Over Time", fontsize=14, pad=15)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("View Count", fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Show the plot interactively
    plt.show()


if __name__ == "__main__":
    generate_view_count_graph()
