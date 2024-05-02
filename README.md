# Wizard City of Weird Fishes - Configuration Tool

This application is a configuration tool designed to display and modify different parameters using a graphical user interface (GUI) created with tkinter. It reads configuration data from a JSON file, presents the parameters to the user, allows modifications, and provides an option to export the modified configuration to a text file.

![Screenshot of Project](https://github.com/QcTL/CoWF-VarImport/assets/71326643/441a91c2-e282-4e74-ac6d-a24dabbf1f79)

## Features

- **Parameter Display**: Displays various parameters based on the provided configuration data.
- **Parameter Modification**: Allows users to modify parameters using different types of input components.
- **Export Functionality**: Provides an option to export the modified configuration to a text file.
- **Supported Parameter Types**: Supports boolean values, integer ranges, sets of values, and text-only categories.

## Requirements

- Python 3.x
- Tkinter library

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Run the `main.py` script.
3. The application will read the configuration data from the `file.json` file provided in the same directory.
4. Modify parameters as needed using the GUI components.
5. Click the "Export" button to save the modified configuration to a text file.
6. Close the application window when finished.

## Additional Notes

- The configuration data should be provided in JSON format, with each parameter represented as a list containing:
  - The type of parameter (`bool`, `int-range`, `set`, `cat`).
  - The values or range of values for the parameter (if applicable).
  - The name of the parameter.
  - A description of the parameter.
- The application automatically creates GUI components based on the type of parameter specified in the configuration data.

