"""
@auth: jodth07
"""
import os
import sys
import json

from io import StringIO
import requests
from requests.exceptions import RequestException


BASE_SITE = "https://trefle.io/api/"


def get_token(base_token, base_site=BASE_SITE) -> str:
    """
    using personal provided token to get access token
    :param base_token: this requires a base token, which can be acquired from the BASE_SITE
    :param base_site: this string is the base url for the api, to be used for authentication
    :return: a session token to be used with token parameters in queries
    """
    if base_token:
        response = requests\
            .post(f"{base_site}auth/claim?token={base_token}&origin=YOUR-WEBSITE-URL")
        session_token: str = response.json()["token"]
        return session_token
    print("base token is missing")
    sys.exit(1)


def get_data(end_point: str, session_token: str, base_site=BASE_SITE) -> list:
    """
    using the different endpoints, create links and pulls data from api
    :param end_point: hierarchical classification / api endpoint to be used in request
    :param session_token: session token of type string to be used in request
    :param base_site: base site for the api calls
    :return: list containing json data
    """
    try:
        data = requests\
            .get(f"{base_site}{end_point}/?token={session_token}")\
            .json()
        return data
    except RequestException:
        print("the request did not succeed")
        return []


def get_str_data(data_li: list) -> StringIO:
    """
    writes data to a string buffer to further processing
    :param data_li: json data in list, to be stored in file.
    :return: a string buffer
    """
    data_io = StringIO()
    for record in data_li:
        data_io.write(f"{record},\n")
    return data_io


def process_data(endpoint_name: str, session_token: str) -> bool:
    """
    use endpoint name to create json file in
    :param endpoint_name: hierarchical classification / api endpoint to be used in request
    :param session_token: session token of type string to be used in request
    :return: true if process completes successfully
    """
    data: list = get_data(endpoint_name, session_token)
    with open(f"data/{endpoint_name}.json", "w") as writer:
        writer.write(json.dumps(data))
        print(f"Data written for {endpoint_name}")
        return True


if __name__ == '__main__':

    endpoints = ["kingdoms", "subkingdoms", "divisions", "families", "genuses", "plants"]
    MY_TOKEN = os.environ.get("MY_TOKEN")
    ss_token = get_token(MY_TOKEN)

    for endpoint in endpoints:
        process_data(endpoint, ss_token)
