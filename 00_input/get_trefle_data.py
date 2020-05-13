import requests
from requests.exceptions import RequestException
import os
from io import StringIO
import json

BASE_SITE = "https://trefle.io/api/"


def get_token(base_token, base_site=BASE_SITE) -> str:
    """
    using personal provided token to get access token
    :return: string token to be used in queries
    """
    if base_token:
        response = requests.post(f"{base_site}auth/claim?token={base_token}&origin=YOUR-WEBSITE-URL")
        return response.json()["token"]
    print("base token is missing")
    exit(1)


def get_data(end_point: str, session_token: str, base_site=BASE_SITE) -> list:
    """
    using the different endpoints, create links and pulls data from api
    :param end_point: hierarchical trees of type strings
    :return: json object
    """
    try:
        return requests.get(f"{base_site}{end_point}/?token={session_token}").json()
    except RequestException as e:
        print("the request did not succeed")
        return exit(1)


def get_str_data(data_li: list) -> StringIO:
    """
    takes in the json data in list, to be stored in file.
    :param data_li:
    :return:
    """
    data_io = StringIO()
    for record in data_li:
        data_io.write(f"{record},\n")
    return data_io


def process_data(endpoint_name:str, session_token:str):
    """
    :param endpoint_name:
    :return:
    """
    data :list = get_data(endpoint_name, session_token)
    with open(f"data/{endpoint_name}.json", "w") as writer:
        writer.write(json.dumps(data))
    print(f"Data written for {endpoint_name}")


if __name__ == '__main__':

    prs = ["kingdoms", "subkingdoms", "divisions", "families", "genuses", "plants"]
    MY_TOKEN = os.environ.get("MY_TOKEN")
    ss_token = get_token(MY_TOKEN)

    for pr in prs:
        process_data(pr, ss_token)
