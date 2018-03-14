def lookup_entry():
    print('lookup')
    return

def set_entry():
    print('set')
    return

def delete_entry():
    print('delete')
    return

def list_entries():
    print('list')
    return

def quit():
    print('quit')
    in_use = False

def use_phonebook():
    in_use = True

    functions = {
        '1': lookup_entry,
        '2': set_entry,
        '3': delete_entry,
        '4': list_entries,
        '5': quit
    }

    instructions = 'Electronic Phone Book\n\
    =====================\n\
    1. Look up an entry\n\
    2. Set an entry\n\
    3. Delete an entry\n\
    4. List all entries\n\
    5. Quit\n'


    while in_use:
        print(instructions)

        ans = str(input("What do you want to do (1-5)? "))
        
        if ans in functions:
            functions[ans]()
        else:
            print("That is not a valid input. Try again.")

if __name__ == '__main__':
    use_phonebook()