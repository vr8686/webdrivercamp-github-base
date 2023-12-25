"""
client_api.py

This module defines the ClientAPI class for handling API requests and return responses.
"""
import requests

from base.components.payload_api import PayloadAPI


class ClientAPI:
    """
    The ClientAPI class provides methods for making HTTP requests using various HTTP methods
    such as GET, POST, PATCH, and DELETE. It also uses the PayloadAPI class for handling
    headers and payload data.

    Methods:
    - get_request(url: str) -> object: Sends a GET request to the specified URL.
    - post_request(url: str) -> object: Sends a POST request to the specified URL.
    - patch_request(url: str) -> object: Sends a PATCH request to the specified URL.
    - delete_request(url: str) -> object: Sends a DELETE request to the specified URL.
    """
    def get_request(self, url: str) -> object:
        """
        Send a GET request to the specified URL.

        Parameters:
            - url (str): The URL to send the GET request to.

        Returns:
            object: The response data from the GET request.
        """
        headers = PayloadAPI().from_json_file().get("headers", {})

        response = requests.get(url,
                                timeout=5,
                                headers=headers,
                                json={}
                                )
        return response

    def post_request(self, url: str) -> object:
        """
        Send a POST request to the specified URL.

        Parameters:
            - url (str): The URL to send the POST request to.

        Returns:
            object: The response data from the POST request.
        """
        headers = PayloadAPI().from_json_file().get("headers", {})
        json = PayloadAPI().from_json_file().get("json", {})

        response = requests.post(url,
                                 timeout=5,
                                 headers=headers,
                                 json=json,
                                 )

        return response

    def patch_request(self, url: str) -> object:
        """
        Send a PATCH request to the specified URL.

        Parameters:
            - url (str): The URL to send the PATCH request to.

        Returns:
            object: The response data from the PATCH request.
        """
        headers = PayloadAPI().from_json_file().get("headers", {})
        json = PayloadAPI().from_json_file().get("json", {})

        response = requests.patch(url,
                                  timeout=5,
                                  headers=headers,
                                  json=json,
                                  )

        return response

    def delete_request(self, url: str) -> object:
        """
        Send a DELETE request to the specified URL.

        Parameters:
            - url (str): The URL to send the DELETE request to.

        Returns:
            object: The response data from the DELETE request.
        """
        headers = PayloadAPI().from_json_file().get("headers", {})
        json = PayloadAPI().from_json_file().get("json", {})

        response = requests.delete(url,
                                   timeout=5,
                                   headers=headers,
                                   json=json,
                                   )

        return response
