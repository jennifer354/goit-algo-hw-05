def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except IndexError:
            return "Invalid command format."

    return inner
    
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Provide both name and phone number.")
    
    name, phone = args
    if not phone.startswith("+380") or not phone[4:].isdigit() or len(phone) != 13:
        raise ValueError("Phone number should be in the format +380XXXXXXXXX.")
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Provide both name and phone number.")
    
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact not found.")
    
    if not phone.startswith("+380") or not phone[4:].isdigit() or len(phone) != 13:
        raise ValueError("Phone number should be in the format +380XXXXXXXXX.")
    
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Provide a name to show the contact.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found.")
    
    return f"Name: {name}, Phone: {contacts[name]}"
@input_error
def show_all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "all":
             show_all_contacts(contacts)    

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()