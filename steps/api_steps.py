from behave import *

from base.components.client_api import ClientAPI
from base.components.context_table import ContextTable
from base.components.payload_api import PayloadAPI
from base.components.response_api import ResponseAPI
from base.helpers import helper


@step("clear JSON data in payload")
def clear_json_data(context):
    PayloadAPI().delete_json_data()


@step("send {api_request} request with authentication to {endpoint}")
@step("send {api_request} request to {endpoint}")
def send_request(context, api_request, endpoint):
    if context.table and api_request == "GET":
        query = context.table.headings[0]
        context.response = ClientAPI().get_request(helper.construct_url(context.BASE_API, endpoint, query))
    else:
        context.response = getattr(ClientAPI(),
                                   f"{api_request.lower()}_request")(helper.construct_url(context.BASE_API, endpoint))


@step('verify status code is {code:d}')
def verify_status(context, code):
    ResponseAPI().verify_status(context.response, code)


@step("verify number of repos is {number:d}")
def verify_number_of_repos(context, number):
    ResponseAPI().verify_number_of_repos(context.response, number)


@step("Add values to payload")
def add_values(context):
    PayloadAPI().to_json_file(ContextTable(context).to_flat_dict())


@step("verify parameters")
def verify_parameters(context):
    ResponseAPI().verify_parameters(parameters=ContextTable(context).to_flat_dict(), response=context.response)
