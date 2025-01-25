import csv
import os
from datetime import datetime
from typing import Dict


class PropertyDataStorage:
    """Class responsible for storing property data in CSV format."""

    def __init__(self, filename: str = "property_data.csv"):
        self.filename = filename
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """Create CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["timestamp", "property_id", "url", "title", "view_count"]
                )

    def store_property_data(self, property_id: str, property_data: Dict) -> None:
        """
        Store property data in CSV format with timestamp.

        Args:
            property_id: The ID of the property
            property_data: Dictionary containing property details
        """
        timestamp = datetime.now().isoformat()

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    timestamp,
                    property_id,
                    property_data.get("url", ""),
                    property_data.get("title", ""),
                    property_data.get("view_count", ""),
                ]
            )
