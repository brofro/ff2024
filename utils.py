import requests


def get_html(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as e:
        return None
