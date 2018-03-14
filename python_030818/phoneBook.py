import pickle
import sys
phoneBook = {}

def lookup_entry():
    try:
        name = str(input("What is the name?"))
        print("Found entry for",name, ":", phoneBook[name])
    except KeyError:
        print("No entry found")
        phonebookapp()
    return

def set_entry():
    name = str(input("Name:"))
    number = input("Phone Number:")
    email = input("Email address:")
    website = input("Website:")
    phoneBook[name] = {'Name': name, 'Phone number': number, 'Email': email, 'Website': website}
    print("Entry stored for", name)
    return

def delete_entry():
    try:
        name = str(input("Name?"))
        del phoneBook[name]
        print("Deleted entry for", name)
    except KeyError:
        print("No entry found.")
        phoneBookapp()
    return

def list_entries():
    for i in phoneBook:
        print("Found entry for", i, ":", phoneBook[i])
    return

def save_entries():
    fh = open('phoneBook.pickle', 'wb')
    pickle.dump(phoneBook, fh)
    fh.close()
    return

def restore_saved_entries():
    with open('phoneBook.pickle', 'rb') as fb:
        phoneBook = pickle.load(fb)
    print(phoneBook)
    return

def quit():
    in_use = False
    sys.exit('Bye.')

def use_phoneBook():
    in_use = True

    functions = {
        '1': lookup_entry,
        '2': set_entry,
        '3': delete_entry,
        '4': list_entries,
        '5': save_entries,
        '6': restore_saved_entries,
        '7': quit
    }

    instructions = 'Electronic Phone Book\n\
    =====================\n\
    1. Look up an entry\n\
    2. Set an entry\n\
    3. Delete an entry\n\
    4. List all entries\n\
    5. Save entries\n\
    6. Restore saved entries\n\
    7. Quit\n'

    while in_use:
        print(instructions)
        ans = str(input("What do you want to do (1-7)? "))
        
        if ans in functions:
            functions[ans]()
        else:
            print("That is not a valid input. Try again.")

if __name__ == '__main__':
    use_phoneBook()