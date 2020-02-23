import requests
import os
from io import StringIO


MY_TOKEN = os.environ.get("MY_TOKEN")
BASE_SITE = "https://trefle.io/api/"


def get_token() -> str:
    """
    using personal provided token to get access token
    :return: string token to be used in queries
    """
    response = requests.post(f"{BASE_SITE}auth/claim?token={MY_TOKEN}&origin=YOUR-WEBSITE-URL")
    return response.json()["token"]


def get_data(end_point: str) -> list:
    """
    using the different endpoints, create links and pulls data from api
    :param end_point: hierarchical trees of type strings
    :return: json object
    """
    try:
        return requests.get(f"{BASE_SITE}{end_point}/?token={token}").json()
    except:
        return []


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


def process_data(endpoint_name):
    """

    :param endpoint_name:
    :return:
    """
    data: list = get_data(endpoint_name)
    data_io: StringIO = get_str_data(data)
    with open(f"{endpoint_name}.json", "w") as writer:
        writer.write(data_io.getvalue())
    print(f"Data written for {endpoint_name}")


if __name__ == '__main__':
    token = get_token()
    prs = ["kingdoms", "subkingdoms", "divisions", "families", "genuses", "plants"]
    for pr in prs:
        process_data(pr)
