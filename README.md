# Booli View Count

A Python application for tracking and analyzing property views on Booli.se. This tool allows you to scrape view count data for specific properties and visualize the trends over time.

## Features

- Scrape property view counts from Booli.se
- Store historical view data in CSV format
- Visualize view count trends using matplotlib
- Track multiple properties simultaneously

## Prerequisites

- Python 3.x
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/booli-view-count.git
cd booli-view-count
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# OR
.\venv\Scripts\activate  # On Windows
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:

```bash
python main.py
```

2. Enter the Booli property ID when prompted

   - The property ID can be found in the URL of the property listing on Booli.se
   - Example: For https://www.booli.se/annons/12345, the ID is 12345

3. The script will:

   - Fetch the current view count
   - Store the data in a CSV file
   - Display the property details

4. To visualize the data:

```bash
python visualize_data.py
```

## Project Structure

- `main.py`: Entry point of the application
- `booli_scraper.py`: Handles web scraping from Booli.se
- `property_storage.py`: Manages data storage in CSV format
- `visualize_data.py`: Creates visualizations of the view count data
- `property_data.csv`: Stores the historical property data

## Dependencies

- requests: For making HTTP requests
- beautifulsoup4: For web scraping
- python-dotenv: For environment variable management
- urllib3: For HTTP client functionality
- pandas: For data manipulation
- matplotlib: For data visualization
