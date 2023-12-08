# AirBnB_clone
## Description of the Project
The Airbnb project is a web application that aims to replicate the core functionality of the popular Airbnb platform. It allows users to list their properties for rent and enables potential guests to browse and book accommodations. The project is built using a variety of technologies, including HTML, CSS, JavaScript, and a Python-based backend.

## Description of the Command Interpreter
The command interpreter is a command-line interface (CLI) tool that interacts with the backend of the Airbnb project. It provides a set of commands to perform various actions such as creating a new property listing, searching for available accommodations, and making bookings. The command interpreter is designed to be user-friendly and efficient, making it easy for developers to manage the application from the terminal.

## How to Start the Command Interpreter
To start the command interpreter, follow these steps:

1 - Clone the repository to your local machine:

`git clone https://github.com/abdo-elshaikh/AirBnB_clone`

2 - Navigate to the project directory:

`cd AirBnB_clone`

3 - Install the required dependencies:

`pip install -r requirements.txt`

4 - Run the command interpreter:

`python interpreter.py`

## How to Use the Command Interpreter
The command interpreter supports a variety of commands. Here are some examples:

- Create a new property listing:

    create_listing --title "Cozy Apartment" --location "City Center" --price 100 --capacity 2

- Search for available accommodations:

    search --location "City Center" --check-in "2023-01-01" --check-out "2023-01-07"

- Make a booking:

    book --listing-id 123 --guest-name "John Doe" --check-in "2023-01-01" --check-out "2023-01-07"

## Examples
Here are some examples of using the command interpreter:

- Creating a new property listing:

    create_listing --title "Spacious Villa" --location "Suburbia" --price 200 --capacity 6

- Searching for available accommodations:

    search --location "Suburbia" --check-in "2023-02-01" --check-out "2023-02-15"

- Making a booking:

    book --listing-id 456 --guest-name "Jane Smith" --check-in "2023-02-01" --check-out "2023-02-15"

## Contributing
To contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.

#### We appreciate your contributions!
