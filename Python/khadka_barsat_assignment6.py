# Program : khadka_barsat_assignment6.py
#
# Programmer: Barsat Khadka
# Date: 19/11/2024
# Description: Program to manage house records using a menu using local files and I/O along with user input.
# Version Required: Python 3.12.9 or greater
#
# Variables Used:
# - houseRecordsList: List that stores all new house records added during the program's execution.
# - houseRecordsFile: List that stores all house records loaded from the file "house.txt".
# - houseId: Stores the unique ID for a house, used to add, delete, find, or edit houses.
# - address: Stores the address of a house.
# - cost: Stores the cost of a house in dollars.
# - sq_ft: Stores the square footage of a house.
# - year_built: Stores the year the house was built.
# - choice: Stores the menu option selected by the user.
# - total: Stores the total inventory value (sum of all house costs).
# - records: used to merge `houseRecordsList` and `houseRecordsFile` for displaying records so that all records are included.
# - matches: List of houses that match the search criteria (e.g., cost) during a search operation.
# - fields: Temporary variable used to split and parse data from each line in the input file ("house.txt").

 
houseRecordsList = []   #House Records List that user can control
houseRecordsFile = []   #House Records File to store records from the file


#Storing on same format as previous List to ensure consistency
with open("house.txt", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            houseRecordsFile.append({
                "id": fields[0],
                "address": fields[1],
                "cost": fields[2],
                "sq_ft": fields[3],
                "year_built": fields[4]
            })



#Display menu and return the input number 
def display_menu():
    print()
    print("Choices For Menu:")
    print("\t1) List Records")
    print("\t2) Add a House")
    print("\t3) Delete a House")
    print("\t4) Find a House")
    print("\t5) Edit House")
    print("\t6) Total Inventory")
    print("\t7) Save record and Exit")
    return input("Please Enter a number (1-5): ")

def list_records():
    records = houseRecordsList + houseRecordsFile
    if not records:
        print("No house records found.")
        return
    print("\nHouse Records:")
    print(f"{'House ID#':<10} | {'Address':<20} | {'Cost($)':<15} | {'Sq Ft':<10} | {'Year Built':<10}")
    print("-" * 70)
    for house in records:
        cost_with_commas = f"{int(house['cost']):,}"
        print(f"{house['id']:<10} | {house['address']:<20} | {cost_with_commas:<15} | {house['sq_ft']:<10} | {house['year_built']:<10}")

# Add a house
def add_house():
    houseId = input("Enter House ID#: ")
    if any(house['id'] == houseId for house in houseRecordsList + houseRecordsFile):
        print("Error: House ID# must be unique.")
        return
    address = input("Enter Address: ")
    cost = input("Enter Cost($): ")
    sq_ft = input("Enter Square Footage: ")
    year_built = input("Enter Year Built: ")
    houseRecordsList.append({
        "id": houseId, "address": address, "cost": cost, "sq_ft": sq_ft, "year_built": year_built
    })
    print("House added successfully.")

# Delete a house
def delete_house():
    houseId = input("Enter House ID# to delete: ")
    for house in houseRecordsList + houseRecordsFile:
        if house['id'] == houseId:
            user_choice = input("Are you sure you want to delete this house? (y/n): ")
            if user_choice.lower() == 'y':
                houseRecordsList.remove(house) if house in houseRecordsList else houseRecordsFile.remove(house)
                print("House deleted.")
                return
    print("Error: House not found.")

# Find a house by ID or cost (user decides through which he wants to find)
def find_house():
    search_option = input("Search by (1) House ID# or (2) Cost? Enter 1 or 2: ")
    if search_option == "1":
        houseId = input("Enter House ID#: ")
        for house in houseRecordsList + houseRecordsFile:
            if house['id'] == houseId:
                print(f"{'House ID#':<10} | {'Address':<20} | {'Cost($)':<15} | {'Sq Ft':<10} | {'Year Built':<10}")
                print("-" * 70)
                cost_with_commas = f"{int(house['cost']):,}"
                print(f"{house['id']:<10} | {house['address']:<20} | {cost_with_commas:<15} | {house['sq_ft']:<10} | {house['year_built']:<10}")
                return
        print("Error: House not found.")
    elif search_option == "2":
        cost = input("Enter Cost($): ")
        matches = [house for house in houseRecordsList + houseRecordsFile if house['cost'] == cost]
        if matches:
            print(f"{'House ID#':<10} | {'Address':<20} | {'Cost($)':<15} | {'Sq Ft':<10} | {'Year Built':<10}")
            print("-" * 70)
            for house in matches:
                print(f"{house['id']:<10} | {house['address']:<20} | {house['cost']:<15} | {house['sq_ft']:<10} | {house['year_built']:<10}")
        else:
            print("No houses found with that cost.")

# Edit a house
def edit_house():
    houseId = input("Enter House ID# to edit: ")
    for house in houseRecordsList + houseRecordsFile:
        if house['id'] == houseId:
            print("Current details:")
            print(house)
            house['address'] = input("Enter new Address: ")
            house['cost'] = input("Enter new Cost($): ")
            house['sq_ft'] = input("Enter new Square Footage: ")
            house['year_built'] = input("Enter new Year Built: ")
            print("House updated successfully.")
            return
    print("Error: House not found.")

# Show total inventory value (the total cost)
def show_total_inventory():
    total = sum(int(house['cost']) for house in houseRecordsList + houseRecordsFile)
    print(f"Total inventory value: ${total:,}")

# Save records to a new file "newhouse.txt"
def save_records():
    with open("newhouse.txt", "w") as file:
        for house in houseRecordsList + houseRecordsFile:
            file.write("\t".join([house['id'], house['address'], house['cost'], house['sq_ft'], house['year_built']]) + "\n")
    print("Records saved to newhouse.txt.")

# Main program loop that integrates all the program
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            list_records()
        elif choice == '2':
            add_house()
        elif choice == '3':
            delete_house()
        elif choice == '4':
            find_house()
        elif choice == '5':
            edit_house()
        elif choice == '6':
            show_total_inventory()
        elif choice == '7':
            save_records()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")

#Calling main to start the program
main()