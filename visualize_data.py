import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates


def load_and_prepare_data() -> pd.DataFrame:
    """Load data from CSV and prepare it for visualization."""
    df = pd.read_csv("property_data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = pd.to_datetime(
        df["timestamp"].dt.date
    )  # Convert to datetime for better plotting
    return df.sort_values("timestamp").groupby("date").last().reset_index()


def setup_plot_style():
    """Configure the visual style of the plot."""
    sns.set_theme(style="darkgrid")
    sns.set_palette("husl")
    plt.figure(figsize=(12, 6))


def create_line_plot(df: pd.DataFrame):
    """Create the main line plot with the data."""
    sns.lineplot(data=df, x="date", y="view_count", marker="o", linewidth=2)
    # Format x-axis to show only dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())


def customize_plot():
    """Add customization elements to the plot."""
    plt.title("Property View Count Over Time (Daily Latest)", fontsize=14, pad=15)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("View Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()


def generate_view_count_graph():
    """Main function to generate the view count visualization."""
    df = load_and_prepare_data()
    setup_plot_style()
    create_line_plot(df)
    customize_plot()
    plt.show()


if __name__ == "__main__":
    generate_view_count_graph()
