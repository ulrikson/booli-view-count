from booli_scraper import BooliScraper
from property_storage import PropertyDataStorage
from visualize_data import generate_view_count_graph

class PropertyTrackerCLI:
    def __init__(self):
        self.scraper = BooliScraper()
        self.storage = PropertyDataStorage()

    def scrape_property_data(self):
        property_id = input("Enter the property ID: ")
        property_details = self.scraper.get_property_details(property_id)

        if property_details:
            print("\nProperty Details:")
            for key, value in property_details.items():
                print(f"{key}: {value}")

            # Store the data in CSV
            self.storage.store_property_data(property_id, property_details)
            print(f"\nData has been stored in {self.storage.filename}")
        else:
            print("Failed to fetch property details")

    def display_menu(self):
        print("\nBooli Property Tracker")
        print("1. Scrape property data")
        print("2. Visualize view count data")
        print("3. Exit")
        return input("Choose an option (1-3): ")

    def run(self):
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.scrape_property_data()
            elif choice == "2":
                generate_view_count_graph()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.") 