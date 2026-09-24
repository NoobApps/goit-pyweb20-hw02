from book import AddressBook
from record import Record
from field import *
from handlers import *


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if len(user_input.strip()) == 0:
            print(f"No command entered: try {list(HANDLERS.keys())}")
            continue
        else:
            command, *args = parse_input(user_input)

        if command in HANDLERS.keys():
            if command in ["close", "exit"]:
                print(book)
                save_data(book)
                print("Goodbye!")
                break

            print(HANDLERS.get(command)(args, book))

        else:
            print(f"Invalid command.try {list(HANDLERS.keys())}")


if __name__ == "__main__":
    main()
