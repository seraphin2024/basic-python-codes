'''
Simple Phonebook
Create a dictionary to store names and phone numbers. Allow the user to:

Add a new contact

View all contacts

Search for a contact by name
'''
#we can use the fucntions and dictionaries here totally :


phn_book = {}

x = input("Do you want to create a phone book? If yes, type 1: ")

while x == "1":
    name = input("Enter the name of the contact: ")
    num = input("Enter the phone number of " + name + ": ")
    

    phn_book[name] = num

    x = input("If you want to stop, enter -1. To add another, enter 1: ")


y = input("\nType 1 to view all contacts.\nType 2 to search a phone number by name.\nYour choice: ")

if y == "1":
    print("\n Your Phone Book:")
    for name, number in phn_book.items():
        print(f"{name}: {number}")

elif y == "2":
    search_name = input("Enter the name to search: ")
    if search_name in phn_book:
        print(f"Phone number of {search_name}: {phn_book[search_name]}")
    else:
        print("Sorry, we don't have that contact.")



