"""
response_api.py

This module defines the ResponseAPI class for verifying API response data.
"""

from jsonpath_ng import parse


class ResponseAPI:
    """
    ResponseAPI class for handling and verifying API responses.

    Methods:
        verify_status: Verifies that the API response status code matches the expected code.
        verify_number_of_repos: Verifies the number of repositories in the API response.
        verify_parameters: Verifies specific parameters in the API response.
        status_decoder: Decodes HTTP status codes into human-readable messages.
    """

    def verify_status(self, response, code) -> None:
        """Verify the API response status code.

        Args:
            response: The API response object.
            code: The expected HTTP status code.

        Raises:
            AssertionError: If the response status code does not match the expected code.
        """
        assert response.status_code == code, (f'API response code does not match:'
                                              f'\nExpected: {code}'
                                              f'\nActual:\t{response.status_code} '
                                              f'({self.status_decoder(response.status_code)})')

    def verify_number_of_repos(self, response: object, expected_number: int) -> None:
        """
        Verify the number of repositories in the API response.

        Args:
            response: The API response object.
            expected_number: The expected number of repositories. Should be as integer.

        Raises:
            AssertionError: If the number of repos in the response does not match the expected.
        """

        # Deserialize response data
        data = response.json()

        # Depending on request, response type can vary. Verify for dict and for list.
        if isinstance(data, dict):
            count = data.get("total_count", None)
            assert count is not None, "Invalid response format. 'total_count' key not found."
        elif isinstance(data, list):
            count = len(data)
        else:
            raise ValueError("Invalid response format. Expected dict or list.")

        assert count == expected_number, (f'Number of repos does not match:'
                                          f'\nExpected: {expected_number}'
                                          f'\nActual:\t{count}'
                                          )

    def verify_parameters(self, parameters: dict, response: object) -> None:
        """
        Verify specific parameters in the API response.

        Args:
            parameters: A dictionary of parameter names and their expected values.
            response: The API response object.

        Raises:
            AssertionError: If any parameter values in the response do not match the expected.
        """
        for key, expected_value in parameters.items():
            jsonpath = f'$..{key}'
            response_key = parse(jsonpath).find(response.json())
            actual_value = response_key[0].value if response_key else None

            assert str(actual_value) == expected_value, (f"Values for key '{key}' do not match. "
                                                         f"Expected: {expected_value}, "
                                                         f"Actual: {actual_value}")

    def status_decoder(self, code: int) -> str:
        """
        Decode HTTP status codes into human-readable messages.

        Args:
            code: The HTTP status code.

        Returns:
            str: Human-readable message corresponding to the provided HTTP status code.
        """
        codes_map = {204: "No content",
                     301: "Moved permanently",
                     304: "Not modified",
                     307: "Temporary Redirect",
                     400: "Bad Request",
                     401: "Requires authentication",
                     403: "Forbidden",
                     404: "Resource not found",
                     422: "Validation failed, or the endpoint has been spammed."}
        if code in codes_map:
            return codes_map[code]

        return "Unknown status code"
