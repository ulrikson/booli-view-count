from booli_scraper import BooliScraper
from property_storage import PropertyDataStorage

if __name__ == "__main__":
    property_id = input("Enter the property ID: ")
    scraper = BooliScraper()
    storage = PropertyDataStorage()

    property_details = scraper.get_property_details(property_id)

    if property_details:
        print("\nProperty Details:")
        for key, value in property_details.items():
            print(f"{key}: {value}")

        # Store the data in CSV
        storage.store_property_data(property_id, property_details)
        print(f"\nData has been stored in {storage.filename}")
    else:
        print("Failed to fetch property details")
