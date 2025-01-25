from booli_scraper import BooliScraper

if __name__ == "__main__":
    property_id = input("Enter the property ID: ")
    scraper = BooliScraper()
    property_details = scraper.get_property_details(property_id)

    if property_details:
        print("Property Details:")
        for key, value in property_details.items():
            print(f"{key}: {value}")
    else:
        print("Failed to fetch property details")
