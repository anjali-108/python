# Location Coordinate Processing System using Tuple

locations = []

while True:

    print("\n===== GPS LOCATION SYSTEM =====")
    print("1. Add Location")
    print("2. Display Locations")
    print("3. Search Location")
    print("4. Update Location")
    print("5. Delete Location")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Location
    if choice == "1":

        name = input("Enter location name: ")
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))

        location = (name, latitude, longitude)
        locations.append(location)

        print("Location added successfully!")

    # Display Locations
    elif choice == "2":

        if len(locations) == 0:
            print("No locations available.")

        else:
            print("\nStored GPS Coordinates:")

            for location in locations:
                print("Name      :", location[0])
                print("Latitude  :", location[1])
                print("Longitude :", location[2])
                print()

    # Search Location
    elif choice == "3":

        name = input("Enter location name to search: ")

        found = False

        for location in locations:

            if location[0] == name:
                print("Location found!")
                print("Name      :", location[0])
                print("Latitude  :", location[1])
                print("Longitude :", location[2])

                found = True
                break

        if not found:
            print("Location not found.")

    # Update Location
    elif choice == "4":

        name = input("Enter location name to update: ")

        for i in range(len(locations)):

            if locations[i][0] == name:

                latitude = float(input("Enter new latitude: "))
                longitude = float(input("Enter new longitude: "))

                locations[i] = (name, latitude, longitude)

                print("Location updated successfully!")
                break

        else:
            print("Location not found.")

    # Delete Location
    elif choice == "5":

        name = input("Enter location name to delete: ")

        for i in range(len(locations)):

            if locations[i][0] == name:

                locations.pop(i)

                print("Location deleted successfully!")
                break

        else:
            print("Location not found.")

    # Exit
    elif choice == "6":

        print("Program ended.")
        break

    else:
        print("Invalid choice!")
