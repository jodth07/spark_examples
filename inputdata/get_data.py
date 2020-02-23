import requests
import os
import json


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


def process_data(endpoint_name):
    """

    :param endpoint_name:
    :return:
    """
    data: list = get_data(endpoint_name)
    with open(f"{endpoint_name}.json", "w") as writer:
        writer.write(json.dumps(data))
    print(f"Data written for {endpoint_name}")


if __name__ == '__main__':
    token = get_token()
    prs = ["kingdoms", "subkingdoms", "divisions", "families", "genuses", "plants"]
    for pr in prs:
        process_data(pr)
