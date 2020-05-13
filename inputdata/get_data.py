import requests
import os
import json


BASE_SITE = "https://trefle.io/api/"


def get_token(base_token : str) -> str:
    """
    using personal provided token to get access token
    :return: string token to be used in queries
    """
    if base_token:
        return requests.post(f"{BASE_SITE}auth/claim?token={base_token}&origin=YOUR-WEBSITE-URL").json()["token"]
    print("base token is missing")
    exit(1)


def get_data(end_point: str, base_site: str = BASE_SITE) -> list:
    """
    using the different endpoints, create links and pulls data from api
    :param end_point: hierarchical trees of type strings
    :param base_site: hierarchical trees of type strings
    :return: json object
    """
    try:
        return requests.get(f"{base_site}{end_point}/?token={token}").json()
    except:
        print("requests was unsuccessful")
        return None


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

    prs = ["kingdoms", "subkingdoms", "divisions", "families", "genuses", "plants"]
    MY_TOKEN = os.environ.get("MY_TOKEN")
    token = get_token(MY_TOKEN)

    for pr in prs:
        process_data(pr)
