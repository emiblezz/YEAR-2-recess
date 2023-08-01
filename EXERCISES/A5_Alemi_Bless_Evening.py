# Exception handling Assignment
def check_in(passenger_name, luggage_weight):
    try:
        if luggage_weight > 20:
            raise ValueError("Exceeded luggage weight limit!")
        else:
            print(f"Passenger {passenger_name} checked in successfully.")
    except ValueError as error:
        print(f"Check-in error: {str(error)}")
    except TypeError as error:
        print(f"Type error occurred: {str(error)}")
    except Exception as error:
        print(f"An unexpected error occurred during check-in: {str(error)}")
    finally:
        print("Check-in process completed.\n")


# Simulating check-in process for passengers
check_in("Alemi Emmanuel", 18)
check_in("Stephen Jeff", 25)
check_in("Michael Akiki", -5)


# file handling Assignment

def write_to_file(file_name, data, mode):
    try:
        with open(file_name, mode) as file:
            file.write(data + '\n')
            print(f"Data written to {file_name} successfully.")
    except IOError:
        print(f"Error writing to {file_name}.")


def read_from_file(file_name, mode):
    try:
        with open(file_name, mode) as file:
            data = file.read()
            print(f"Data read from {file_name}:")
            print(data)
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except IOError:
        print(f"Error reading from {file_name}.")


# Writing and reading using different file modes
write_to_file("file.txt", "Hello, World!", 'w')  # Write mode
write_to_file("file.txt", "Goodbye!", 'a')  # Append mode
read_from_file("file.txt", 'r')  # Read mode
write_to_file("file.txt", "Overwritten data!", 'w')  # Write mode (overwrite)
read_from_file("file.txt", 'r+')  # Read-write mode
write_to_file("file.txt", "New line!", 'a+')  # Append-read mode
read_from_file("file.txt", 'w+')  # Write-read mode
