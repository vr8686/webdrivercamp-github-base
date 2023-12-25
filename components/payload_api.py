"""
payload_api.py

This module defines the PayloadAPI class, which provides methods for managing JSON payload data
using file operations. The class allows reading, updating, and deleting JSON data stored in a file.
"""
import json
import os

from jsonpath_ng import parse


class PayloadAPI:
    """
    A class for managing JSON payload data using file operations.

    Attributes:
    - DIR_PATH: The directory path where the script is located.
    - FILE_NAME: The complete path to the payload JSON file.

    Methods:
    - from_json_file: Reads JSON data from the file and returns it as a dictionary.
    - to_json_file: Updates the JSON data in the file based on JSONPath.
    - delete_json_data: Deletes the value for the "json" key and sets it to an empty dictionary.
    """

    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    FILE_NAME = f"{DIR_PATH}/payload.json"

    def from_json_file(self) -> dict:
        """
        Reads JSON data from the file and returns it as a dictionary.

        Returns:
        - dict: The JSON data from the file.
        """
        try:
            with open(self.FILE_NAME, "r", encoding='utf-8') as file:
                data = json.load(file)

                return data

        except FileNotFoundError:
            # Raise error if the file is not found and print error message
            print(f"Error: File '{self.FILE_NAME}' not found.")
            raise

    def to_json_file(self, data_object) -> None:
        """
        Updates the JSON data in the file based on JSONPath.

        Parameters:
        - data_object: The dictionary containing data to be updated in the file for 'json' key.
        """
        try:
            with open(self.FILE_NAME, "r", encoding='utf-8') as file:
                json_data = json.load(file)

            # Update the 'json' key using JSONPath
            jsonpath = parse("$.json")
            match = jsonpath.find(json_data)

            if match:
                match[0].value.update(data_object)
            else:
                # If the 'json' key is not present, create it
                json_data["json"] = data_object

            # Write updated 'json' data to the file
            with open(self.FILE_NAME, "w", encoding='utf-8') as file:
                json.dump(json_data, file, indent=2)

        except FileNotFoundError:
            print(f"Error: File '{self.FILE_NAME}' not found.")
            raise

    def delete_json_data(self):
        """
        Deletes the value for the "json" key and sets it to an empty dictionary.
        Prints a message indicating that the data has been deleted.
        """
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Delete the value for the "json" key and set it to an empty dictionary
            data['json'] = {}

            # Write the updated content back to the file
            with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)

            # Print success message
            print(f"JSON data in {self.FILE_NAME} has been deleted")

        except FileNotFoundError:
            print(f"Error: File '{self.FILE_NAME}' not found.")
            raise
